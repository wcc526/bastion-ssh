import logging
import pyte
from bastion_ssh.plugins.ssh.ssh_filter import SSHFilter
from bastion_ssh.utils import get_console_dimensions

LOG = logging.getLogger(__name__)


class AuditCMDFilter(SSHFilter):
    def __init__(self, context):
        self.context = context
        self.stream = pyte.ByteStream()
        width, height = get_console_dimensions()
        self.screen = pyte.Screen(columns=width, lines=height)
        self.stream.attach(self.screen)

    def before_channel(self, x):
        self.stream.feed(x)
        for line in self.screen.display:
            LOG.info(line)

    def before_stdin(self, x):
        pass

    def when_resize(self):
        width, height = get_console_dimensions()
        self.screen.resize(columns=width, lines=height)
