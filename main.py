from pdf_extractor import extract_text_from_pdf
from text_processor import process_text_file
from qa_system import QASystem
from summarizer import TextSummarizer
from config import config

def main():
    text_file = 'extracted_text.txt'
    extracted_text = extract_text_from_pdf(config['pdf_path'], text_file)
    
    passages = process_text_file(extracted_text, max_words_per_passage=200)
    
    summarizer = TextSummarizer(config['summarizer_model'])
    summary = summarizer.summarize_text(extracted_text, max_length=150, min_length=30)
    print(f'\n{'='*70}\n')
    print('Document summary:', summary)
    print(f'\n{'='*70}\n')

    qa = QASystem(config['qg_model'], config['qa_model'])
    qa.answer_questions([passages[1]])
    print('The Q&A above were generated based on paragraph 2.')

if __name__ == '__main__':
    main()