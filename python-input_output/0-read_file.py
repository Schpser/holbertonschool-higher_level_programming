#!/usr/bin/python3

def read_file(filename=""):
        """Reads and prints a text file's content.
    Args:
        filename (str): File path to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end="")
