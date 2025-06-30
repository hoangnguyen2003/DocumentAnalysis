import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def process_text_file(input_file):
    with open(input_file, "r") as file:
        document_text = file.read()

    sentences = sent_tokenize(document_text)
    
    passages = []
    current_passage = ""
    for sentence in sentences:
        if len(current_passage.split()) + len(sentence.split()) < 200:
            current_passage += " " + sentence
        else:
            passages.append(current_passage.strip())
            current_passage = sentence
    if current_passage:
        passages.append(current_passage.strip())
    
    return passages

if __name__ == "__main__":
    passages = process_text_file("extracted_text.txt")
    print(f"Processed text into {len(passages)} passages")