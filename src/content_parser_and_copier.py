from pdfminer.high_level import extract_text
from selenium.webdriver.common.keys import Keys

# from tabula import read_pdf


def pdf_text_extractor(pdf_filepath):
    text = extract_text(pdf_filepath)
    return text

def web_scraper(url):


"""
We'll get back to him...

def table_extractor(pdf_filepath):
    tables = read_pdf(pdf_file, pages='all')
    return tables

"""
