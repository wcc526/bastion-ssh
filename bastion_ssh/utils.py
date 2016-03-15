#!/usr/bin/env python
# coding: utf-8
import struct
import fcntl
import sys
import termios


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
