import random
import collections

guess_menu = "Please guess your number:\n"


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        rand_set = set()
        while len(rand_set) < self.difficulty:
            x = random.randint(0, 101)
            rand_set.add(x)
        print(rand_set)
        return rand_set

    def get_list_from_user(self):
        user_set = set()
        while len(user_set) < self.difficulty:
            x = int(input(f"Please guess your number between 1 to  101 \n"))
            # if x not in user_set:
            user_set.add(x)
        print(user_set)
        return user_set

    def is_list_equal(self):

        if self.generate_sequence() == self.get_list_from_user():
            return 'True'
        else:
            return 'False'

    def run(self):
        if self.is_list_equal() == 'True':
            print("You WIN")
        else:
            print("You lost, try again")
