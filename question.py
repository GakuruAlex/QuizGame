class Question:
    """_Model of Question_
    """
    def __init__(self, text: str, answer: bool):
        """_Construct Question object_

        Args:
            text (_str_): _Question text_
            answer (_boolean_): _Answer to the Question_
        """
        self.text = text
        self.answer = answer
    def __str__(self):
        return self.text +" "+ self.answer