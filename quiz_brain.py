class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.questions_list = q_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Thats Right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is: {correct_answer}")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1

        answer = input(f"Q.{self.question_number} {current_question.text}. (True/False)?: ").lower()


