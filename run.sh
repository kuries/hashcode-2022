#!/bin/bash
for file in Test_Dataset/*.txt; do
    echo $file;
    python3 main.py $file;
done

