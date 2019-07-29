#!/bin/bash
# Created on 20 July 2019 by Joshua Scriven
# Uses Pandoc to create Academic PDF from multiple md files nested in <5 levels
# IMPORTANT: set bib tex file path in .txt file.

cd -- "$(dirname "$BASH_SOURCE")"


# Ignores notes and drafts by requiring underscore for inclusion
pandoc `( ls **.md **/**.md **/**/**.md **/**/**/**.md)` -o extracted_annotations_`date +%d_%b_%Y__%H_%M_%S`.pdf --filter pandoc-citeproc --toc

osascript -e 'tell application "Terminal" to close first window'
