#!/usr/bin/python

""" Module for converting CSV files to JSON format """

import csv
import json

csv_filepath = 'data.csv'
json_filepath = 'data.json'


def convert_csv_to_json(csv_filepath):
    data = []

    try:
        with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        with open("data.json", mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
