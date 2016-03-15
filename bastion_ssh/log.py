#!/usr/bin/env python
# coding: utf-8

import logging
import logging.handlers
import os
from logging.config import dictConfig

default_formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s",
    "%d/%m/%Y %H:%M:%S")
DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'paramiko': {
            'level': 'WARNING'
        }
    }
}


def configure_logging():
    def_logpath = os.path.join(os.getenv('USERPROFILE') or os.getenv('HOME'), 'bastion_ssh.log')
    dictConfig(DEFAULT_LOGGING)
    file_handler = logging.handlers.RotatingFileHandler(def_logpath, maxBytes=10485760, backupCount=300,
                                                        encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # file_handler.setFormatter(default_formatter)
    console_handler.setFormatter(default_formatter)

    logging.root.setLevel(logging.DEBUG)
    logging.root.addHandler(file_handler)
    logging.root.addHandler(console_handler)
