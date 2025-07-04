from transformers import pipeline
from question_generator import QuestionGenerator
import re

class QASystem:
    def __init__(self, qg_model, qa_model):
        self.qa_pipeline = pipeline('question-answering', model=qa_model)
        self.qg = QuestionGenerator(qg_model)
    
    def answer_questions(self, passages):
        answered_questions = set()

        for passage in passages:
            questions = self.qg.generate_questions(passage)
            for question in questions:
                if question not in answered_questions:
                    answer = self.qa_pipeline({'question': question, 'context': passage})
                    print(f'Q: {question}')
                    print(f'A: {re.sub(r'\s+', ' ', answer['answer'].strip())}\n')
                    answered_questions.add(question)
            print(f'{'='*70}\n')