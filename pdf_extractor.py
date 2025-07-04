import pathlib, pymupdf

def extract_text_from_pdf(pdf_path, output_text_file):
    with pymupdf.open(pdf_path) as pdf:
        extracted_text = ''
        for page in pdf:
            extracted_text += page.get_text()

    pathlib.Path(output_text_file).write_bytes(extracted_text.encode())

    print(f'Text extracted and saved to {output_text_file}.')
    return extracted_text