#!/usr/bin/env python3

import sys
import subprocess


if len(sys.argv) != 2:
    print("Usage: ./changeJane.py oldFiles.txt") #prior step is save the filenames into a txt
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
for line in lines:
    print("line\n",line)
    line=line.strip().split()
    username=line[1]
    print("username\n",username)
    old_filename = line[2]
    print("old_filename:\n",old_filename)
    if username == "jane":
        new_filename=old_filename.replace("jane", "jdoe")
        print("new_filename:\n",new_filename)
        try:
            subprocess.run(['mv', "/home/student-03-fdee3db0e36f/" + old_filename, "/home/student-03-fdee3db0e36f/"+new_filename])
            print("Renamed {} to {}".format(old_filename, new_filename))
        except Exception as e:
            print(e)
