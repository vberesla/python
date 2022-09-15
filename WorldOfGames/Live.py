from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import GuessGame
from MemoryGame import MemoryGame

game_menu = "Please choose a game to play:\n\t1. Memory Game - a sequence of numbers will appear for 1 second and you " \
            "have to guess it back\n\t2. Guess Game - guess a number and see if you chose like the " \
            "computer\n\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
difficulty_menu = "Please choose game difficulty from 1 to 5:\n"


def validation_input(number, limit):
    if 0 < number <= limit:
        return True
    else:
        print("Your option is wrong, your choice should be between 0 to " + str(limit))
        return False


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play"


def load_game():
    game_number = int(input(game_menu))
    while validation_input(game_number, 3) is False:
        game_number = int(input(game_menu))
    game_diff = int(input(difficulty_menu))
    while validation_input(game_diff, 5) is False:
        game_diff = int(input(difficulty_menu))

    if game_number == 1:
        game = MemoryGame(game_diff)
        game.run()
    elif game_number == 2:
        game = GuessGame(game_diff)
        game.run()
    elif game_number == 3:
        game = CurrencyRouletteGame(game_number)
        game.run()
    else:
        print("Game Over")
