#!/usr/bin/env python
# coding: utf-8
import os
import sys
import tty
import select
import signal
import paramiko
import termios
import logging
from bastion_ssh.plugins.ssh.ssh_transport import SSHTransport
from bastion_ssh.utils import get_console_dimensions

LOG = logging.getLogger(__name__)


class InteractiveShell(object):
    def __init__(self, context, input=sys.stdin, output=sys.stdout):
        self.ssh_transport = SSHTransport(context=context)
        width, height = get_console_dimensions()
        self.channel = self.ssh_transport.transport.open_session()
        paramiko.agent.AgentRequestHandler(self.channel)
        self.channel.get_pty(term=os.getenv('TERM') or 'vt100', width=width, height=height)
        self.channel.invoke_shell()
        signal.signal(signal.SIGWINCH, self.sigwinch)
        self.input = input
        self.output = output
        self.listeners = []

    def sigwinch(self, signal, data):
        # We do as little as possible when the WINCH occurs!!
        self.channel.resize_pty(*get_console_dimensions())
        for listener in self.listeners:
            listener.when_resize()

    def process_channel(self, channel):
        """Process the given channel."""
        if channel.closed:
            return False

        if channel.recv_ready():
            try:
                data = channel.recv(4096)

                if not data:
                    return False

                for listener in self.listeners:
                    listener.before_channel(data)

                # self.audit_cmd.audit_channel(data)
                self.output.write(data)
                self.output.flush()

            except Exception:
                pass

        if channel.exit_status_ready():
            return False

        return True

    def process_stdin(self, channel):
        """Read data from stdin and send it over the channel."""
        try:
            buf = os.read(self.input.fileno(), 1)
        except OSError:
            buf = None
        if not buf:
            return False
        for listener in self.listeners:
            listener.before_stdin(buf)
        channel.send(buf)
        return True

    def handle_communications(self):
        while True:
            try:
                r, w, x = select.select([self.input, self.channel], [], [], 5)
            except Exception:
                pass

            if self.channel in r:
                if not self.process_channel(self.channel):
                    break

            if self.input in r:
                if not self.process_stdin(self.channel):
                    self.channel.shutdown_write()
                    break

    def shell(self):
        """Open a shell."""
        # Make sure we can restore the terminal to a working state after
        # interactive stuff is over
        oldtty = None
        try:
            oldtty = termios.tcgetattr(self.input.fileno())

            # Set tty mode to raw - this is a bit dangerous because it stops
            # Ctrl+C working! But that is required so that you can Ctrl+C
            # remote things
            tty.setraw(self.input.fileno())

            # For testing you could use cbreak mode - here Ctrl+C will kill the
            # local yaybu instance but otherwise is quite like raw mode
            # tty.setcbreak(self.input.fileno())

            # We want non-blocking mode, otherwise session might hang
            # This might cause socket.timeout exceptions, which we just ignore
            # for read() operations
            self.channel.settimeout(0.0)

            self.handle_communications()
        except Exception, e:
            LOG.warn(e, exc_info=True)
        finally:
            if oldtty:
                termios.tcsetattr(self.input.fileno(), termios.TCSADRAIN, oldtty)
            self.channel.close()

    def attach(self, sshfilter):
        """Adds a given ssh filter to the listener queue.
        """
        self.listeners.append(sshfilter)
