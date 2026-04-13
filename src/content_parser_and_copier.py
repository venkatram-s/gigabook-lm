from os import makedirs, path
from sys import platform
from fitz import open


def litebook_parser(pdf_path, vault_dir="research_vault"):
    base_filename = path.basename(pdf_path)
    doc_name = path.splitext(base_filename)[0]

    doc_workspace = path.join(vault_dir, doc_name)
    asset_folder = path.join(doc_workspace, "assets")

    makedirs(asset_folder, exist_ok=True)

    output_md_path = path.join(doc_workspace, f"{doc_name}.md")

    try:
        doc = open(pdf_path)
        md_output = []

        for page_num, page in enumerate(doc, start=1):
            md_output.append(f"\n\n## --- Page {page_num} ---\n")

            # --- A. TEXT EXTRACTION ---
            blocks = page.get_text("blocks")
            for b in blocks:
                clean_text = b[4].replace("\u2002", " ").replace("\u2003", " ")
                md_output.append(clean_text)

            # --- B. IMAGE EXTRACTION ---
            image_list = page.get_images(full=True)
            for img_idx, img in enumerate(image_list, start=1):
                xref, width, height = img[0], img[2], img[3]

                if width < 40 or height < 40:
                    continue

                base_image = doc.extract_image(xref)
                image_ext = base_image["ext"]

                image_name = f"pg{page_num}_img{img_idx}.{image_ext}"
                # Path relative to the script for writing
                image_write_path = path.join(asset_folder, image_name)
                # Path relative to the Markdown file for linking
                image_rel_link = f"assets/{image_name}"

                with open(image_write_path, "wb") as f:
                    f.write(base_image["image"])

                md_output.append(f"\n\n> ![Image]({image_rel_link})\n\n")

        doc.close()

        # 2. SAVE TO MD FILE
        full_markdown = "\n".join(md_output)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(full_markdown)

        return True

    except Exception as e:
        return False


# --- EXECUTION ---
if __name__ == "__main__":
    if platform == "win32":
        system("chcp 65001 > nul")

    # This creates research_vault/table/table.md and research_vault/table/assets/
    var = litebook_parser("E:\Resources\PDFS\windows-via-c-c_5th-edition.pdf")
