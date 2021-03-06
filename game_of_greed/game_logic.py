import collections
import random


class GameLogic:
    """
    Description: Builds GameLogic objects for rolling dice calculating points scored from dice rolls

    Methods
    __init__
        Args:
            self: GameLogic object instance containing dice roll generation and point scoring rules
            score: Integer for points accumulated from dice rolls
            roll_round: Under development
        Returns:
            None

    roll_dice
        Args:
            dice_count: Integer for number of dice rolled during a game round
        Returns:
            dice_holder: Tuple of integers representing 1-6 dice rolls

    calculate_score
        Args:
            self: Tuple of integers representing 1-6 dice rolls
        Returns:
            score: Integer of points yielded from dice roll combinations
    """

    def __init__(self, score=0, roll_round=0):
        # self.dice_roll = dice_roll
        self.score = score
        self.roll_round = roll_round

    @staticmethod
    def roll_dice(dice_count=0):
        dice_holder = []
        for i in range(dice_count):
            dice_holder.append(random.randint(1, 6))
        dice_holder = tuple(dice_holder)
        return dice_holder

    @staticmethod
    def calculate_score(self):
        counter = collections.Counter(self)
        score = 0
        commonest = counter.most_common()

        if len(counter) == 6:
            score += 1500
            return score

        elif len(counter) == 3 and commonest[0][1] == 2 and commonest[1][1] == 2 and commonest[2][1] == 2:
            score += 1500
            return score

        elif len(counter) == 2 and (commonest[0][1] == 3 and commonest[1][1] == 3):
            if commonest[0][0] == 1:
                score += 1000
            else:
                score += commonest[0][0] * 100
            if commonest[1][0] == 1:
                score += 1000
            else:
                score += commonest[1][0] * 100
            return score

        elif len(counter) == 1 and commonest[0][1] == 6:
            if commonest[0][0] == 1:
                score += 4000
                return score
            else:
                score += commonest[0][0] * 400
                return score

        else:
            for item in commonest:
                if item[1] == 5:
                    if item[0] == 1:
                        score += 3000
                    else:
                        score += item[0] * 300
                elif item[1] == 4:
                    if item[0] == 1:
                        score += 2000
                    else:
                        score += item[0] * 200
                elif item[1] == 3:
                    if item[0] == 1:
                        score += 1000
                    else:
                        score += item[0] * 100
                elif item[1] == 2:
                    if item[0] == 1:
                        score += 200
                    elif item[0] == 5:
                        score += 100
                elif item[1] == 1:
                    if item[0] == 1:
                        score += 100
                    elif item[0] == 5:
                        score += 50

            return score

    # def validate_keepers(rolled, user_selected):


if __name__ == "__main__":
    new_game = GameLogic()

    new_game.roll_dice(4)
    new_game.calculate_score((5, 6, 2, 4, 4, 1))
