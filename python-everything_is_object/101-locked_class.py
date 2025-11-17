#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """LockedClass that prevents dynamic attributes except first_name"""
    __slots__ = ['first_name']
