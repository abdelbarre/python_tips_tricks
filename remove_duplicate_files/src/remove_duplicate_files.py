#!/usr/bin/env python
# coding: utf-8
# Libs Import
import os
import sys

file_path = "../folder/"
file_list = os.listdir(file_path) # List all files in file path

for file_name in file_list:
    if "(1)" not in file_name:  ## you can change the duplicate symbol/word (e.g [original_name]copy.toto ) 
        continue
    original_file_name = file_name.replace('(1)', '') # replace the duplication symbol/word by '' to get the original name of file
    print(file_name)
    print(original_file_name)
    if not os.path.exists(os.path.join(file_path, original_file_name)) : ## return true if the file exists :
        continue  # do not remove files which have no original
    os.remove(os.path.join(file_path, file_name))