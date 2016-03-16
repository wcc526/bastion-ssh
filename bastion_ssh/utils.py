#!/usr/bin/env python
# coding: utf-8
import struct
import fcntl
import sys
import termios
import re


def get_console_dimensions():
    """
    This function use to get the size of the windows!
    """
    width, height = 80, 24
    try:
        fmt = 'HH'
        buffer = struct.pack(fmt, 0, 0)
        result = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, buffer)
        height, width = struct.unpack(fmt, result)
    except Exception, e:
        pass
    finally:
        return width, height


def command_parser(ps1_command):
    """
    :param ps1_command: which contain ps1.
    :return: user's input command
    """
    ret = None
    ps1_pattern = re.compile('(\[.*@.*\][\$#])(.*)')
    match = ps1_pattern.search(ps1_command)
    if match:
        ret = match.group(2).strip()
    return ret
