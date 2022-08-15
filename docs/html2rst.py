import os
import re
import sys
import utils
import pypandoc

# Define constants
HTMLS_PATH = './Documentation'
PATH_INDEX = './docs/source/index.rst'
OUTPUT_PATH = './docs/source/converted'
EXCEPTIONS_CLEAN = ['ChangeLog', 'LogIt']
EXTERNAL_EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.pptx', '.odg', '.png', '.jpg', '.jpeg', '.gif',  '.cmake']

if __name__ == '__main__':

  # Download pandoc binary
  pypandoc.pandoc_download.download_pandoc()

  # Get list of HTML files
  files = utils.get_files(HTMLS_PATH, EXTERNAL_EXTENSIONS)
  html_files, external_files, note_files = files

  # Copy current assets to output directory
  utils.copy_external(HTMLS_PATH, OUTPUT_PATH, EXTERNAL_EXTENSIONS)

  # Parse HTML files to RST
  utils.parse_html_files(html_files, HTMLS_PATH, OUTPUT_PATH)

  # Update index content (table of contents)
  utils.update_index(
    html_files,
    external_files,
    note_files,
    PATH_INDEX,
    EXCEPTIONS_CLEAN
  )

  exit(0)
