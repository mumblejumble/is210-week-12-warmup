#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Exception Class"""
    pass


def get_age(birthyear):
    """Function that tests age"""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError()
    else:
        return age
