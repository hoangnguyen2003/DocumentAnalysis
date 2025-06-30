from pdf_extractor import extract_text_from_pdf
from text_processor import process_text_file
from qa_system import QASystem
from summarizer import TextSummarizer

def main():
    pdf_path = "google_terms_of_service_en_in.pdf"
    text_file = "extracted_text.txt"
    extract_text_from_pdf(pdf_path, text_file)
    
    passages = process_text_file(text_file)
    
    print("\n=== SUMMARY ===")
    with open(text_file, "r") as file:
        document_text = file.read()
    
    summarizer = TextSummarizer()
    summary = summarizer.summarize_text(document_text)
    print("Document summary:", summary)

    print("\n=== QA SYSTEM ===")
    qa = QASystem()
    qa.answer_questions(passages[:1])

if __name__ == "__main__":
    main()