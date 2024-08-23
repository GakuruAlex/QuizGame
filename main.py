from data import question_data
from question import Question
def main() -> None:
    
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))
    
    print(question_bank)

if __name__ =="__main__":
    main()