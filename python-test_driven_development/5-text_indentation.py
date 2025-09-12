#!/usr/bin/python3
"""
Module 5-text_indentation
Contains function to print text with new lines after . ? :
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return

    result = ""
    i = 0
    n = len(text)

    while i < n:
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end="")
