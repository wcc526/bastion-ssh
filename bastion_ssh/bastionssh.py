#!/usr/bin/env python
# coding: utf-8


import logging

LOG = logging.getLogger(__name__)

from bastion_ssh.log import configure_logging
from bastion_ssh.context import Context
from bastion_ssh.plugins.audit.main import AuditCMDFilter
from bastion_ssh.plugins.ssh.main import InteractiveShell
from bastion_ssh.argparser import get_parser
from bastion_ssh import __version__
import sys


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(__version__)
        return

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args['hostname'] and args['username']:
        hostname = args['hostname']
        username = args['username']
        port = 22
        if args['port']:
            port = args['port']
        context = Context(hostname=hostname, username=username, port=port)
        interactiveshell = InteractiveShell(context)

        auditcmdfilter = AuditCMDFilter(context)
        interactiveshell.attach(auditcmdfilter)

        interactiveshell.shell()


if __name__ == '__main__':
    configure_logging()
    command_line_runner()
