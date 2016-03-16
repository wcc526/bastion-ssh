# -*- coding: utf-8 -*-
from pyte.streams import ByteStream
import logging

LOG = logging.getLogger(__name__)


class BetterStream(ByteStream):
    def __init__(self):
        super(BetterStream, self).__init__()
