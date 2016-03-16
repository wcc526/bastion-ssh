from __future__ import print_function
import logging
from bastion_ssh.plugins.ssh.ssh_filter import SSHFilter
from bastion_ssh.utils import get_console_dimensions
from bastion_ssh.plugins.audit.screen import BetterScreen
from bastion_ssh.plugins.audit.stream import BetterStream
import os

LOG = logging.getLogger(__name__)


class AuditCMDFilter(SSHFilter):
    def __init__(self, context):
        self.context = context
        self.stream = BetterStream()
        width, height = get_console_dimensions()
        self.screen = BetterScreen(columns=width, lines=height)
        self.stream.attach(self.screen)
        self.input_mode = False
        self.command_path = os.path.join(os.getenv('USERPROFILE') or os.getenv('HOME'), 'bastion_command.log')
        self.channel_path = os.path.join(os.getenv('USERPROFILE') or os.getenv('HOME'), 'bastion_channel.log')

    def before_channel(self, x):
        self.stream.feed(x)
        with open(self.channel_path, "ab+") as f:
            for line in self.screen.display:
                print(line, file=f)

    def before_stdin(self, x):
        self.input_mode = True
        if str(x) in ['\r', '\n', '\r\n']:
            with open(self.command_path, "ab+") as f:
                print(self.screen.get_command(), file=f)
            self.input_mode = False

    def when_resize(self):
        width, height = get_console_dimensions()
        self.screen.resize(columns=width, lines=height)
