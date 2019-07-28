#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Uses the pdfannots.py script, created by Andrew Baumann (https://github.com/0xabu/pdfannots).
Baumann's script "extracts annotations from a PDF file in a text format for use in reviewing."
I simply loop all PDF files in the current directory as arguments in Baumann's script, setting each output text file name to the repective PDF name.
For this to work, set the output file name to "test.txt" in the o option (e.g., -o "test.txt")
"""

import os, re, sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)
print (ROOT_PATH)

for file in os.listdir(ROOT_PATH):
   if file.endswith(").pdf"):
    print(file)
    args = ' '.join(map(str, sys.argv[1:]))
    args = re.sub(r'test', re.escape(file), args)
    os.system("/Volumes/MAC\ HD/joshuascriven/Desktop/python\ tests/pdfannots.py " + re.escape(file) + " " + args)
