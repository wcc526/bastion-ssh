import paramiko
import socket
import time
import logging
from paramiko.ssh_exception import SSHException
import bastion_ssh.errors

LOG = logging.getLogger(__name__)


class SSHTransport(object):
    """ This object wraps a shell in yet another shell. When the shell is
    switched into "simulate" mode it can just print what would be done. """

    def __init__(self, context):
        self.context = context
        self.connection_attempts = 20
        self.transport = None
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for tries in range(self.connection_attempts):
            try:
                self.client.connect(hostname=self.context.hostname,
                                    username=self.context.username,
                                    port=self.context.port,
                                    allow_agent=True,
                                    look_for_keys=True)
                break
            except paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException:
                LOG.warning("Unable to authenticate with remote server")
                raise bastion_ssh.errors.ConnectionError(
                    "Unable to authenticate with remote server")
            except (socket.error, EOFError):
                LOG.warning("connection refused. retrying.")
                time.sleep(tries + 1)
        else:
            self.client.close()
            raise bastion_ssh.errors.ConnectionError(
                "Connection refused %d times, giving up." % self.connection_attempts)
        self.transport = self.client.get_transport()
        self.transport.set_keepalive(30)
        self.transport.use_compression(True)

    def __del__(self):
        self.client.close()
