from transformers import pipeline

class TextSummarizer:
    def __init__(self, model):
        self.summarizer = pipeline('summarization', model=model)
    
    def summarize_text(self, text, max_length, min_length):
        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        
        sentences = [s.strip() for s in summary[0]['summary_text'].split('.') if s.strip()]
        standardized_sentences = []
        for sentence in sentences:
            standardized = sentence[0].upper() + sentence[1:].lower() + '.'
            standardized_sentences.append(standardized)
        standardized_text = ' '.join(standardized_sentences)

        return standardized_text