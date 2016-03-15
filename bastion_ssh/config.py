import glob
from ConfigParser import SafeConfigParser, NoSectionError, NoOptionError
from os.path import expanduser


class Config(object):
    """A ConfigParser wrapper to support defaults when calling instance
    methods, and also tied to a single section"""

    def __init__(self, section=None, values=None, extra_sources=()):
        if section is None:
            sources = self._getsources()
            self.cp = SafeConfigParser()
            self.cp.read(sources)
            for fp in extra_sources:
                self.cp.readfp(fp)
        else:
            self.cp = SafeConfigParser(values)
            self.cp.add_section(section)

    def _getsources(self):
        sources = [expanduser('~/.bastion_ssh.ini')]
        return sources

    def _getany(self, method, section, option, default):
        try:
            return method(section, option)
        except (NoSectionError, NoOptionError):
            if default is not None:
                return default
            raise

    def get(self, section, option, default=None):
        return self._getany(self.cp.get, section, option, default)

    def getint(self, section, option, default=None):
        return (int)(self._getany(self.cp.get, section, option, default))

    def getfloat(self, section, option, default=None):
        return (float)(self._getany(self.cp.get, section, option, default))

    def getboolean(self, section, option, default=None):
        return (bool)(self._getany(self.cp.get, section, option, default))

    def items(self, section, default=None):
        try:
            return self.cp.items(section)
        except (NoSectionError, NoOptionError):
            if default is not None:
                return default
            raise
