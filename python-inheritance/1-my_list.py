#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """A class that inherits from list"""
    
    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
