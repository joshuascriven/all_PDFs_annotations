#!/usr/bin/env python
# coding: utf-8

"""
Uses the pdfannots.py script, created by Andrew Baumann (https://github.com/0xabu/pdfannots).
Baumann's script "extracts annotations from a PDF file in a text format for use in reviewing."
I simply loop all PDF files in the current directory as arguments in Baumann's script, setting each output text file name to the repective PDF name.
For this to work, set the output file name to "test.txt" in the o option (e.g., -o "test.txt")
"""
import datetime
import os
import re
from pathlib import Path # for Mac + Win compatability
ROOT_PATH = os.getcwd()
print(Path)
for filename in Path.cwd().rglob('*.pdf'):
	ex = Path(str({filename}))
	# print(ex.stem)
	pdfname = ex.stem
	pdfname = pdfname.replace(" ","_")
	f1=open(Path(ROOT_PATH+"/log.txt"), "a")
	f1.write(pdfname+" highlights saved: " + str(datetime.datetime.now())[0:19].replace(":","_") + "\n")
	f1.close()
	os.system(f'"""{ROOT_PATH}/pdfannots.py""" """{filename}""" """-o""""{pdfname}""".md""""')