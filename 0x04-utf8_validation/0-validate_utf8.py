#!/usr/bin/python3
"""Contain a function to validate UTF-8 encoding"""


def validUTF8(data):
    """Validate if the input integer is a valid utf encoding"""
    if type(data) is not list:
        return False
    for item in data:
        if type(item) is not int:
            return False
        byte_version = item.to_bytes(4, 'big')
        try:
            return bool(byte_version.decode('utf-8'))
        except UnicodeDecodeError:
            return False
