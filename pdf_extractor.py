import fitz

def extract_text_from_pdf(pdf_path, output_text_file):
    pdf = fitz.open(pdf_path)
    extracted_text = ""
    for page in pdf:
        extracted_text += page.get_text()

    with open(output_text_file, "w") as text_file:
        text_file.write(extracted_text)

    print(f"Text extracted and saved to {output_text_file}")
    return output_text_file

if __name__ == "__main__":
    pdf_path = "google_terms_of_service_en_in.pdf"
    output_text_file = "extracted_text.txt"
    extract_text_from_pdf(pdf_path, output_text_file)