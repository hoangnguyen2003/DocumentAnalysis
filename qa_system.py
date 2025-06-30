from transformers import pipeline
from question_generator import QuestionGenerator
from text_processor import process_text_file

class QASystem:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
        self.qg = QuestionGenerator()
    
    def answer_questions(self, passages):
        answered_questions = set()

        for idx, passage in enumerate(passages):
            questions = self.qg.generate_questions(passage)
            for question in questions:
                if question not in answered_questions:
                    answer = self.qa_pipeline({'question': question, 'context': passage})
                    print(f"Q: {question}")
                    print(f"A: {answer['answer']}\n")
                    answered_questions.add(question)
            print(f"{'='*50}\n")

if __name__ == "__main__":
    passages = process_text_file("extracted_text.txt")
    qa = QASystem()
    qa.answer_questions(passages[:1])