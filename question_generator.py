from transformers import pipeline
from text_processor import process_text_file

class QuestionGenerator:
    def __init__(self):
        self.qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
    
    def generate_questions(self, passage, min_questions=3):
        input_text = f"generate questions: {passage}"
        results = self.qg_pipeline(input_text)
        questions = results[0]['generated_text'].split('<sep>')
        
        questions = [q.strip() for q in questions if q.strip()]
        
        if len(questions) < min_questions:
            passage_sentences = passage.split('. ')
            for i in range(len(passage_sentences)):
                if len(questions) >= min_questions:
                    break
                additional_input = ' '.join(passage_sentences[i:i+2])
                additional_results = self.qg_pipeline(f"generate questions: {additional_input}")
                additional_questions = additional_results[0]['generated_text'].split('<sep>')
                questions.extend([q.strip() for q in additional_questions if q.strip()])
        
        return questions[:min_questions]

if __name__ == "__main__":
    passages = process_text_file("extracted_text.txt")
    qg = QuestionGenerator()
    
    for idx, passage in enumerate(passages[:1]):
        questions = qg.generate_questions(passage)
        print(f"Passage {idx+1}:\n{passage}\n")
        print("Generated questions:")
        for q in questions:
            print(f"- {q}")
        print(f"\n{'-'*50}\n")