#!/usr/bin/env bash

count=1
cat file.txt | while read line
do
    if [ $count -eq 10 ]
    then
        echo "$line"
        break
    else
        count=$[ $count + 1 ]
    fi
done 
