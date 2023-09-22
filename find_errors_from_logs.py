#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
    error = input("What is the error? ")
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = error.lower().split()
            returned_errors = [log for log in file.readlines() if all(re.search(i, log.lower()) for i in error_patterns)]
    return returned_errors

def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./find_error.py </home/student-03-934df9665d13/data/fishy.log>")
        sys.exit(1)

    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
