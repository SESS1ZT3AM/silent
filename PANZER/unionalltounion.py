#!/usr/bin/env python

"""
S3SS1Z T3AM'S PROJECT
"""

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces instances of UNION ALL SELECT with UNION SELECT counterpart

    >>> tamper('-1 UNION ALL SELECT')
    '-1 UNION SELECT'
    """

    return payload.replace("UNION ALL SELECT", "UNION SELECT") if payload else payload
