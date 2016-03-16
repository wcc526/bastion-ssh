# -*- coding: utf-8 -*-
from pyte.screens import Screen
import operator
import logging
from bastion_ssh.utils import command_parser

LOG = logging.getLogger(__name__)


class BetterScreen(Screen):
    def __init__(self, columns, lines):
        super(BetterScreen, self).__init__(columns=columns, lines=lines)

    def get_command(self):
        command = None
        for line in reversed(self.buffer):
            x = "".join(map(operator.attrgetter("data"), line)).strip()
            if len(x) > 0:
                command = command_parser(x)
                if command is not None:
                    break
        return command
