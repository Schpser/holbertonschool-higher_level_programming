#!/usr/bin/python3
class LockedClass:
    """A locked class that only lets you create 'first_name' attribute"""
    __slots__ = ('first_name')
