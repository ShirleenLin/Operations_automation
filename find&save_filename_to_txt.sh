#!/bin/bash

> oldFiles.txt  #create
while read -r line; do
    username=$(echo "$line" | cut -d' ' -f2)
    if [ "$username" = "jane" ]; then
        echo "$line" >> oldFiles.txt  #output
    fi
done < /home/student-03-fdee3db0e36f/data/list.txt   #input
