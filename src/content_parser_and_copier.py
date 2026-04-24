from os import makedirs, path
from sys import platform
import fitz
from basictools import if_file_exists,logger

def pdf_parser(pdf_path, notebook_name):
    makedirs(notebook_name, exist_ok=True)

    asset_folder = path.join(notebook_name, "assets")
    makedirs(asset_folder, exist_ok=True)

    base_filename = path.basename(pdf_path)
    doc_name = path.splitext(base_filename)[0]
    output_md_path = path.join(notebook_name, f"extracted_{doc_name}.md")

    try:
        file = fitz.open(pdf_path)
        md_output = []

        for page_num, page in enumerate(file, start=1):
            md_output.append(f"\n\n## --- {base_filename} | Page {page_num} ---\n")

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

        print(logger(f"Success! {pdf_path} has been processed!"))

    except Exception as e:
        print(logger(f"[!] Mission Failed: {e}"))

def text_processor(filepath,notebook_name):
    if not (if_file_exists(filepath)):
        makedirs(notebook_name, exist_ok=True)
        base_filename = path.basename(filepath)
        doc_name = path.splitext(base_filename)[0]
        output_md_path = path.join(notebook_name, f"extracted_{doc_name}.md")

        source=open(filepath,'r')
        source_data=source.read()
        source.close()

        with open(output_md_path, "w", encoding="utf-8") as md_file:
            md_file.write("\n".join(source_data[i]))

         print(logger(f"Success! {filepath} has been processed!"))
    else:
        print(logger(f"File does not exist!"))

def master_combiner(filename,output_file):
   if (filename.startswith("extracted_"):
       if not(remember_Me(filename)):
           with open(output_file,"a+",encoding="utf-8") as destination:
               with open(filename,"r",encoding="utf-8") as source:
                   destination.writelines(source.readlines())
       else:
           logger(f"{filename} was already processed GigaBook-LM!")
   else:
       logger(f"{filename} was not processed by GigaBook-LM!")

def chunk_provider(input_file):
    with open(input_file,"r",encoding="utf-8") as f:
        x=f.read()
