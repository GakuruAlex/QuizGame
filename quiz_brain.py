class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.questions_list = q_bank
        self.score = 0

    def still_has_questions(self) -> bool:
        """_Check if there are more questions_

        Returns:
            bool: _True if more questions are in the question list otherwise False_
        """
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """_Check if user answer is correct_

        Args:
            user_answer (str): _Answer given by user_
            correct_answer (str): _The correct answer to the question_
        """
        if user_answer == correct_answer.lower():
            print("Thats Right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score {self.score}/{self.question_number}")

    def next_question(self) -> None:
        """_Get the next question_
        """
        current_question = self.questions_list[self.question_number]
        self.question_number += 1

        answer = input(f"Q.{self.question_number} {current_question.text}. (True/False)?: ").lower()
        self.check_answer(answer, current_question.answer)


