#!/usr/bin/python3
"Write a function that reads a text file (UTF8) and prints it to stdout:"


def read_file(filename=""):
    """Reads and prints a text file's content.
    Args:
        filename (str): File path to read
    """

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end="")
