import time
# uncomment for testing:
# from game_of_greed.game_logic import GameLogic
# from game_of_greed.banker import Banker

# uncomment for main:
from game_logic import GameLogic
from banker import Banker


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
        self.round_num = 1
        self._roller = roller or GameLogic.roll_dice
        self._calculate = GameLogic.calculate_score

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

        response = input("> ").lower()

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):
        num_die_to_roll = 6
        while self.round_num < 21:
            # Dice rolling starts here!
            rolled_die = self._roller(num_die_to_roll)
            print(f"Starting round {self.round_num}")
            print(f"Rolling {num_die_to_roll} dice...")
            time.sleep(1)
            for_printing = print_die(num_die_to_roll, rolled_die)
            print(f"*** {for_printing}***")

            # Farkle before choosing dice logic here:
            possible_farkle = self._calculate(rolled_die)
            if possible_farkle <= 0:
                print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                num_die_to_roll = 6
                self.banker.clear_shelf()
                print(f"You banked 0 points in round {self.round_num}")
                print(f"Total score is {self.banker.balance} points")
                self.round_num += 1
                continue

            print("Enter dice to keep, or (q)uit:")
            dice_or_quit = input("> ").lower()

            if dice_or_quit == 'q':
                self.quit_game()
                break
            else:
                converted_die = convert_to_int(dice_or_quit)

                # runs the validator to check if the user cheated, returns the length of new dice to roll:
                check, returned_input = self.validator(
                    num_die_to_roll, rolled_die, converted_die)
                converted_validated = convert_to_int(returned_input)
                print('returned_input', converted_validated)
                if check:
                    shelf_points = self._calculate(converted_validated)
                    to_subtract = len(converted_validated)
                    num_die_to_roll -= to_subtract

                    self.banker.shelf(shelf_points)
                    print(
                        f"You have {self.banker.shelved} unbanked points and {num_die_to_roll} dice remaining")
                    print(f"(r)oll again, (b)ank your points or (q)uit:")
                    roll_bank_quit = input("> ").lower()
                    if roll_bank_quit == 'r':
                        if num_die_to_roll == 0:
                            num_die_to_roll = 6
                        continue
                    elif roll_bank_quit == 'b':
                        print(
                            f'You banked {self.banker.shelved} points in round {self.round_num}')
                        self.banker.bank()
                        print(f'Total score is {self.banker.balance} points')
                        self.round_num += 1
                        num_die_to_roll = 6
                        continue
                    elif roll_bank_quit == 'q':
                        self.quit_game()
                        break

    def validator(self, dice_rolled, rolling_die, user_input):
        listed = list(rolling_die)
        for i in user_input:
            if int(i) in listed:
                listed.remove(int(i))
            else:
                print("Cheater!!! Or possibly made a typo...")
                for_printing = print_die(dice_rolled, rolling_die)
                print(f"*** {for_printing}***")
                new_input = input('Enter dice to keep, or (q)uit:\n> ')
                if new_input == 'q':
                    self.quit_game()
                    break
                else:
                    return self.validator(dice_rolled, rolling_die, new_input)

        return True, user_input

    def quit_game(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')


def print_die(dice_print, rolled):
    for_printing = ""
    for num in range(dice_print):
        for_printing += f"{str(rolled[num])} "
    return for_printing

# used to convert a tuple into ints


def convert_to_int(dice_tup):
    returning_die = []
    list_die = list(dice_tup)
    for nums in list_die:
        returning_die.append(int(nums))
    return returning_die


if __name__ == "__main__":
    game = Game()
    game.play()
