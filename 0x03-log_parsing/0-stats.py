#!/usr/bin/python3
"""Read from stdin and parse the input"""
import sys
import re

regx = (r'^([1-2]?\d?\d?\.?){4} - \[\d{4}(-\d{2}){2} '
        r'(\d{2}:){2}\d+\.\d+\] "GET \/projects\/260 HTTP\/1.1" \d+ \d+$')
status_codes = {}
total_size = 0
line_count = 0
allowed_codes = [200, 301, 400, 401, 403, 404, 405, 500]
try:
    for line in sys.stdin:
        # If an input line doesn't match the pattern, we do nothing
        if re.match(regx, line):
            status_and_size = re.search(r'\d+ \d+$', line).group().split(' ')
            status = int(status_and_size[0])
            size = int(status_and_size[1])

            if not status_codes.get(status) and status in allowed_codes:
                status_codes.update({status: 1})

            else:
                status_codes.update({status:
                                     status_codes[status] + 1})
            total_size += size
            line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for k, v in status_codes.items():
                print("{}: {}".format(k, v))


finally:
    print("File size: {}".format(total_size))
    for k, v in status_codes.items():
        print("{}: {}".format(k, v))
