import os
import requests
import pandas as pd
from io import StringIO

SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/gviz/tq?tqx=out:csv'
URL_PDF = 'https://link.springer.com/content/pdf/{codigo_libro}.pdf'
BASE_DIR = '.'
def download_pdfs_from_url(book_url, book_title, book_topic):
    try:
        r = requests.get(book_url)
        url_base = r.url
        codigo_libro = url_base.split('/')[-1]
        url_pdf = URL_PDF.format(codigo_libro = codigo_libro)
        pdf_file = requests.get(url_pdf)
        pdf_file_name = '{base_dir}/{book_topic}/{book_title}.pdf'.format(book_topic=book_topic, book_title=book_title, base_dir=BASE_DIR)
        open(pdf_file_name, 'wb').write(pdf_file.content)
    except:
        print("Error downloading: {book_topic} - {book_title}".format(book_topic=book_topic, book_title=book_title))

response = requests.get(SPREADSHEET_URL)
spreadsheet_csv = StringIO(response.content.decode('utf-8'))

df = pd.read_csv(spreadsheet_csv)

list_of_topics = df['English Package Name'].unique().tolist()

#  creo una carpeta por topico
for topic in list_of_topics:
    folder_name = '{base_dir}/{topic}'.format(base_dir=BASE_DIR, topic=topic)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

df.apply(lambda row: download_pdfs_from_url(row['OpenURL'], row['Book Title'], row['English Package Name']), axis=1)
