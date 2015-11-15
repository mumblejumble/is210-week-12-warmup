#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Exception handling

    Args:
        var1(mixed): first argument.
        var2(mixed): second argument.

    Examples:
        >>> simple_lookup([1,2],4)
        Warning: Your index/key doesn't exist.
        [1, 2]
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist. \n{}'
        return var1
