#!/usr/bin/python3
""" Module for serializing a dictionary to an XML file. """

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Save a dictionary to an XML file. """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load a dictionary from an XML file. """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for elem in root:
        dictionary[elem.tag] = elem.text
    return dictionary
