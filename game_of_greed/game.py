import time
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        # self.round_num = 0 change this back later
        self.round_num = 1

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):
        # TODO: um, the game
        while self.round_num < 21:
            if not self.banker.shelved:
                rolled_die = self._roller(6)
                print(f"Starting round {self.round_num}")
                print(f"Rolling 6 dice...")
                time.sleep(1)
                print(f"*** {rolled_die[0]} {rolled_die[1]} {rolled_die[2]} {rolled_die[3]} {rolled_die[4]} {rolled_die[5]} ***")
                print("Enter dice to keep, or (q)uit:")
                dice_or_quit = input("> ")
                if dice_or_quit == 'q':
                    self.quit_game()
                    break

        # self.round_num += 1 add this after bank/farkle
        pass

    def quit_game(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')

if __name__ == "__main__":
    game = Game()
    game.play()
