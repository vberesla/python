import random
from forex_python.converter import CurrencyRates

guess_menu = "Please guess your number:\n"


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money(self):
        cr = CurrencyRates()
        return cr.convert('USD', 'EUR', 1)

    def get_money_interval(self):
        total_money = self.get_money()
        money_interval_list = [total_money - (5 - self.difficulty), total_money + (5 - self.difficulty)]
        return money_interval_list

    def get_guess_from_user(self):
        return float(input(f"enter a guess of value to a given amount of USD \n"))

    def compare_results(self):
        money_interval_list = self.get_money_interval()
        if money_interval_list[0] <= self.get_guess_from_user() >= money_interval_list[1]:
            return True
        else:
            return False

    def run(self):
        if self.compare_results() == True:
            print("You WIN")
        else:
            print("You lost, try again")
