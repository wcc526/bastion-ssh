import unittest
from bastion_ssh.utils import command_parser

class TestCommandParser(unittest.TestCase):
    def test_genernal_command_parser(self):
        ps1_command = "0;vagrant@cyberivy-test-dev002-shjj:~[vagrant@cyberivy-test-dev002-shjj ~]$ ls"
        self.assertEquals(command_parser(ps1_command), "ls")

    def test_special_command_parser(self):
        ps1_command = "[vagrant@cyberivy-test-dev002-shjj ~]$ cd"
        self.assertEquals(command_parser(ps1_command), "cd")

    def test_genernal_space_command_parser(self):
        ps1_command = "0;vagrant@cyberivy-test-dev002-shjj:~[vagrant@cyberivy-test-dev002-shjj ~]$ cat 1.txt >> 2.txt"
        self.assertEquals(command_parser(ps1_command), "cat 1.txt >> 2.txt")

    def test_null_command_parser(self):
        ps1_command = "0;vagrant@cyberivy-test-dev002-shjj:~[vagrant@cyberivy-test-dev002-shjj ~]$"
        self.assertEquals(command_parser(ps1_command), "")

    def test_special_space_command_parser(self):
        ps1_command = "[vagrant@cyberivy-test-dev002-shjj ~]$ cd /var/tmp && dd"
        self.assertEquals(command_parser(ps1_command), "cd /var/tmp && dd")

    def test_not_special_space_command_parser(self):
        ps1_command = "[vagrant ~]$ cd /var/tmp && dd"
        self.assertEquals(command_parser(ps1_command), None)