#!/usr/bin/python3
"""Read from stdin and parse the input"""
import sys
import re

regx = r'^([1-2]?\d?\d?\.?){4} - \[\d{4}(-\d{2}){2} (\d{2}:){2}\d+\.\d+\] "GET \/projects\/260 HTTP\/1.1" \d+ \d+$'
status_codes = {}
total_size = 0
line_count = 0
try:
    for line in sys.stdin:

        if re.match(regx, line):
            status_and_size = re.search(r'\d+ \d+$', line).group().split(' ')

            if not status_codes.get(status_and_size[0]):
                status_codes.update({status_and_size[0]: 1})

            else:
                status_codes.update({status_and_size[0]:
                                     status_codes[status_and_size[0]] + 1})
            total_size += int(status_and_size[1])
            line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for k, v in status_codes.items():
                print("{}: {}".format(k, v))


finally:
    print("File size: {}".format(total_size))
    for k, v in status_codes.items():
        print("{}: {}".format(k, v))
