import getpass


class Context(object):
    def __init__(self, hostname, username, port=22):
        self.hostname = hostname
        self.username = username
        self.port = port
        self.user = getpass.getuser()
