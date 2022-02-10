#!/bin/bash
for file in Test_Dataset/*.txt; do
    python3 main.py $file;
done

