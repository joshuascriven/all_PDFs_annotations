# all_PDFs_annotations
 Extracts annotations from all PDF files within script path folder.

 Some users might need to run the following code to get Terminal/cmd permissions for both python scripts:

    sudo chmod 777 

## Required files

### `hightlighted_pdf` Folder
This folder should contain all the PDFs with highlights that you wish to extract. For information on extracted annotations, see: [here](https://github.com/0xabu/pdfannots)

### One-click files (on Mac)
- `makePDF.command` 
- `makeMds.command` this runs a shell script to call `pdfannots_scriven.py`

### Files for editing or for use in Terminal or cmd
- `pdfannots_scriven.py` this scripts calls a generic pandoc markdown to PDF and markdown to HTML compilation for the concatenated markdown documents in the "hightlighted_pdf" folder. 
- `pdfannots.py` this is a script created by Andrew Baumann [0xabu](https://github.com/0xabu/pdfannots), that I lightly-edited.

## Output files
- `log.txt` containts the names of each pdf that had highlights extracted, with timestamps
- `extracted_annotations_....pdf` PDF output of annotations from all input PDFs.
- `extracted_annotations_....html` Standalone HTML output of annotations from all input PDFs.

## Other requirements
- Pandoc
- Python 3.x
- Latex distribution (for the PDF)