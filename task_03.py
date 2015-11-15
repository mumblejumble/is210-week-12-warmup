#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger Class"""

    def __init__(self, logfilename):
        """Constructor for CustomError class

        Args:
            logfilename(mixed): logfilename of CustomError Class

        Attributes:
            logfilename(mixed): logfilename of CustomError Class
            msgs(list): list of tuples.
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Log function"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush function that logs error

        Attributes:
            handled(list): handled list of error message.
        """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as my_error:
            self.log('Can\'t open logfile')
            raise my_error

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            self.log('Can\'t write logfile')
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
