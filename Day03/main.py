from question_model import Question
from data import *
from quiz_brain import *

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("you have complete this quiz")
print(f" you score is {quiz.score}/{quiz.question_number}")
