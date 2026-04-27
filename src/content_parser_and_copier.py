from os import makedirs, path
from sys import platform
import fitz
from src.basictools import if_file_exists, logger
from shutil import copyfileobj

def pdf_parser(pdf_path, notebook_name):
    makedirs(notebook_name, exist_ok=True)

    asset_folder = path.join(notebook_name, "assets")
    makedirs(asset_folder, exist_ok=True)

    base_input_file = path.basename(pdf_path)
    doc_name = path.splitext(base_input_file)[0]
    output_md_path = path.join(notebook_name, f"extracted_{doc_name}.md")

    try:
        file = fitz.open(pdf_path)
        md_output = []

        for page_num, page in enumerate(file, start=1):
            md_output.append(f"\n\n## --- {base_input_file} | Page {page_num} ---\n")
            page_dict = page.get_text("dict")
            for b in page_dict["blocks"]:
                if b["type"] == 0:
                    for line in b["lines"]:
                        for span in line["spans"]:
                            clean_text = (
                                span["text"]
                                .replace("\u2002", " ")
                                .replace("\u2003", " ")
                            )
                            md_output.append(clean_text)

                elif b["type"] == 1:
                    if b["width"] < 40 or b["height"] < 40:
                        continue

                    img_name = f"{doc_name}_pg{page_num}_idx{b['number']}.{b['ext']}"
                    img_write_path = path.join(asset_folder, img_name)

                    with open(img_write_path, "wb") as image:
                        image.write(b["image"])

                    md_output.append(f"\n\n![Image](assets/{img_name})\n\n")

        file.close()

        with open(output_md_path, "w", encoding="utf-8") as md_file:
            md_file.write("\n".join(md_output))

        print(logger(f"Success! {pdf_path} has been processed as extracted_{doc_name}.md!"))

    except Exception as e:
        print(logger(f"[!] Mission Failed: {e}"))


def text_processor(filepath, notebook_name):
    if not (if_file_exists(filepath)):
        makedirs(notebook_name, exist_ok=True)
        base_input_file = path.basename(filepath)
        doc_name = path.splitext(base_input_file)[0]
        output_md_path = path.join(notebook_name, f"extracted_{doc_name}.md")

        source = open(filepath, "r")
        source_data = source.read()
        source.close()

        with open(output_md_path, "w", encoding="utf-8") as md_file:
            md_file.write("\n".join(source_data[i]))

        print(logger(f"Success! {filepath} has been processed!"))
    else:
        print(logger(f"File does not exist!"))


def master_file_creator(input_file, output_file):
    if input_file.startswith("extracted_"):
        if not (remember_Me(input_file)):
            with open(output_file, "ab", encoding="utf-8") as destination, open(input_file, "rb", encoding="utf-8") as source:
             copyfileobj(source,destination)
        else
            logger(f"{input_file} was already processed GigaBook-LM!")


def chunk_provider(input_file):
    pass
