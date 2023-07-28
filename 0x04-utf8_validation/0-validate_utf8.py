#!/usr/bin/python3
"""Contain a function to validate UTF-8 encoding"""


def single_byte(n):
    """Return 8 last significant bits of a single number"""
    n_in_bytes = bin(n).split('b')[1]
    if len(n_in_bytes) >= 8:
        return n_in_bytes[-8:]
    else:
        return n_in_bytes.zfill(8)


def utf8length(byte):
    """Find the length of a utf8 encoding"""
    if byte.startswith('11110'):
        return 4
    elif byte.startswith('1110'):
        return 3
    elif byte.startswith('110'):
        return 2
    else:
        return 1


def validUTF8(data):
    """Validate if the input integer is a valid utf encoding"""
    if type(data) is not list:
        return False

    proceed = False
    bytes_left = 0
    for integer in data:
        if type(integer) is not int:
            return False
        last_byte = single_byte(integer)
        if not proceed:
            if last_byte.startswith('10'):
                return False
            bytes_left = utf8length(last_byte) - 1
        else:
            if not last_byte.startswith('10'):
                return False
            bytes_left -= 1
        if bytes_left > 0:
            proceed = True
        else:
            proceed = False
    if bytes_left > 0:
        return False
    return True
