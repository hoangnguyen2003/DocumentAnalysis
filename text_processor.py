import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def process_text_file(document_text, max_words_per_passage):
    sentences = sent_tokenize(document_text)
    
    passages = []
    current_passage = ''
    for sentence in sentences:
        if len(current_passage.split()) + len(sentence.split()) <= max_words_per_passage:
            current_passage += ' ' + sentence
        else:
            passages.append(current_passage.strip())
            current_passage = sentence
    if current_passage:
        passages.append(current_passage.strip())
    
    return passages