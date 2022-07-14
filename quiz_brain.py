class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_no = 0
        self.score = 0

    def ask_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's correct!")
        else:
            print("Oops! That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_no}.\n")

    def print_final_score(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{self.question_no}.\n")

    def still_has_questions(self):
        return self.question_no < len(self.question_list)
