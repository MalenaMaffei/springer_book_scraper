# Springer Books Scraper

This script simply goes through all the books in this spreadsheet https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview?urp=gmail_link and downloads them into different folders (that it previously created) according to each book's topic.
The base directory where the books are downloaded is by default the one where this script is run in. To change it, change the constant `BASE_DIR` to whatever you like, such as `BASE_DIR = /home/books/springer_books` 

### Running the script
`python ./springer_book_scraper.py`


