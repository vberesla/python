import random

guess_menu = "Please guess your number:\n"


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = self.generate_number()
        print(self.secret_number)

    def generate_number(self):
        return random.randint(0, self.difficulty)

    def get_guess_from_user(self):
        return int(input(f"Please guess your number between 1 to {self.difficulty} \n"))

    def compare_results(self):
        if self.secret_number == self.get_guess_from_user():
            return 'True'
        else:
            return 'False'

    def run(self):
        if self.compare_results() == 'True':
            print("You WIN")
        else:
            print("You lost, try again")
