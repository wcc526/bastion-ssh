import argparse
import json


class FromJSON():
    def __init__(self, string):
        self.string = string

    def decode(self):
        return json.loads(self.string)


def get_parser():
    parser = argparse.ArgumentParser(description='bastion SSH host via the command line')
    parser.add_argument('--hostname', '-H', type=str, help='the hostname to connect')
    parser.add_argument('--username', '-u', type=str, help='the username to connect')
    parser.add_argument('--port', '-p', help='select port of ssh(default: 22)', default=22, type=int)
    parser.add_argument('-v', '--version', help='displays the current version of bastion ssh',
                        action='store_true')
    return parser
