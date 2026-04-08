from pdfminer.high_level import extract_text


def text_extractor(pdf_filepath):
    text = extract_text(pdf_filepath)
    return text


pdf_filepath = input()
print(text_extractor(pdf_filepath))
