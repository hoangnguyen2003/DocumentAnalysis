from transformers import pipeline

class QuestionGenerator:
    def __init__(self, model):
        self.qg_pipeline = pipeline('text2text-generation', model=model)
    
    def generate_questions(self, passage, min_questions=3):
        results = self.qg_pipeline(f'generate questions: {passage}')
        questions = results[0]['generated_text'].split('<sep>')
        
        questions = [q.strip() for q in questions if q.strip()]
        
        passage_sentences = passage.split('. ')
        for i in range(len(passage_sentences)):
            if len(questions) >= min_questions:
                break
            additional_input = '. '.join(passage_sentences[i:i+2])
            additional_results = self.qg_pipeline(f'generate questions: {additional_input}')
            additional_questions = additional_results[0]['generated_text'].split('<sep>')
            questions.extend([q.strip() for q in additional_questions if q.strip()])
        
        return questions[:min_questions]