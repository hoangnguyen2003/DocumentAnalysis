from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="t5-small")
    
    def summarize_text(self, text, max_length=150, min_length=30):
        input_text = text[:1000]
        summary = self.summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']

if __name__ == "__main__":
    with open("extracted_text.txt", "r") as file:
        document_text = file.read()
    
    summarizer = TextSummarizer()
    summary = summarizer.summarize_text(document_text)
    print("Summary:", summary)