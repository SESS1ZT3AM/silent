#!/usr/bin/env python

"""
S3SS1Z T3AM'S PROJECT
"""

import re

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOWEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces AND and OR logical operators with their symbolic counterparts (&& and ||)

    >>> tamper("1 AND '1'='1")
    "1 %26%26 '1'='1"
    """

    retVal = payload

    if payload:
        retVal = re.sub(r"(?i)\bAND\b", "%26%26", re.sub(r"(?i)\bOR\b", "%7C%7C", payload))

    return retVal
