from data import question_data
from question import Question
from quiz_brain import QuizBrain
def main() -> None:

    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))

    quiz = QuizBrain(question_bank)
    quiz.next_question()

if __name__ =="__main__":
    main()