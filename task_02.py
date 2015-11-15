#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Exception Class"""
    pass


def get_age(birthyear):
    """Function that tests age

    Args:
        birthyear(int): birthyeat being passed in.

    Attributes:
        age(int): calculates age.

    Returns:
        age if no error, otherwise error.

    Examples:
        >>> get_age(1989)
        26
        >>> get_age(2016)

        Traceback (most recent call last):
        File "<pyshell#1>", line 1, in <module>
          get_age(2016)
        File "/home/vagrant/Desktop/is210-week-12-warmup/task_02.py", line 27,
        in get_age raise InvalidAgeError()
        InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError()
    else:
        return age
