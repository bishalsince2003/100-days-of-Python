from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

# question1 = question("2+3=5",True)
# print(question1.text)
question_bank=[]

for ques in question_data:
    new_question= Question(ques["text"],ques["answer"])
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
