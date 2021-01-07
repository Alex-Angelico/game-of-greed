import time
#uncomment for testing:
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

#uncomment for main:
# from game_logic import GameLogic
# from banker import Banker


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
        # TODO: um, the game
        num_die_to_roll = 6
        while self.round_num < 21:
            # if num_die_to_roll == 0 and self.banker.shelved > 0:
            #     print('Farkle!')  
            for_printing = ""

            # Dice rolling starts here!
            rolled_die = self._roller(num_die_to_roll)
            for num in range(num_die_to_roll):
                for_printing += f"{str(rolled_die[num])} "
            print(f"Starting round {self.round_num}")
            print(f"Rolling {num_die_to_roll} dice...")
            time.sleep(1)
            print(f"*** {for_printing}***")

            # # Farkle before choosing dice logic here:
            # possible_farkle = self.helper_calc(rolled_die)
            # #print('possible_farkle', possible_farkle)
            # if possible_farkle <= 0:
            #     print('FARKLE! No points!')
            #     self.round_num += 1
            #     num_die_to_roll = 6
            #     self.banker.clear_shelf()
            #     print("self.banker.shelved", self.banker.shelved)
            #     continue
            # # Farkle logic end

            print("Enter dice to keep, or (q)uit:")
            dice_or_quit = input("> ").lower()
            # print(type(dice_or_quit)) It's a string currently
            if dice_or_quit == 'q':
                self.quit_game()
                break
            else:
                int_die = []
                list_die = list(dice_or_quit)
                for nums in list_die:
                    int_die.append(int(nums))
                #print(int_die) # this is now a list of ints
                shelf_points = self._calculate(int_die)
                to_subtract = len(int_die)
                num_die_to_roll = num_die_to_roll - to_subtract

                # Farkle Logic
                # if shelf_points > 0 and num_die_to_roll == 0:
                #     print('Farkle!')
                #     num_die_to_roll = 6
                #     self.round_num += 1
                #     continue
                # Farkle Logic

                print(f"You have {shelf_points} unbanked points and {num_die_to_roll} dice remaining")
                print(f"(r)oll again, (b)ank your points or (q)uit:")
                roll_bank_quit = input("> ").lower()
                if roll_bank_quit == 'r':
                    self.banker.shelf(shelf_points)
                    #print(self.banker.shelved) # Does have points
                    continue
                elif roll_bank_quit == 'b':
                    self.banker.shelf(shelf_points)
                    print(f'You banked {self.banker.shelved} points in round {self.round_num}')
                    self.banker.bank()
                    print(f'Total score is {self.banker.balance} points')
                    self.round_num += 1
                    num_die_to_roll = 6
                    continue
                elif roll_bank_quit == 'q':
                    self.quit_game()
                    break

                ############################
                # verification stretch goal (not completed):
                # for die in rolled_die:
                #     print("rolled_die:")
                #     print(die)
                #     for each in list_die:
                #         print("list_die:")
                #         print(each)
                # if int_die == die:
                #     print('True')
                #     break
                # else:
                #     print('False')
                #     break
                ############################

        # self.round_num += 1 add this after bank/farkle
        # pass

    def quit_game(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')

    # Farkle Logic for later
    # def helper_calc(self, points):
    #     int_die = []
    #     list_die = list(points)
    #     for nums in list_die:
    #         int_die.append(int(nums))
    #         #print(int_die) # this is now a list of ints
    #     shelf_points = self._calculate(int_die)
    #     return shelf_points

if __name__ == "__main__":
    game = Game()
    game.play()
