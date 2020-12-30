import collections


class GameLogic:

    def __init__(self, score=0, roll_round=0):
        # self.dice_roll = dice_roll
        self.score = score
        self.roll_round = roll_round

    @staticmethod
    def calculate_score(self):
        counter = collections.Counter(self)
        score = 0
        commonest = counter.most_common()
        if len(counter) == 6:
            score += 1500
            print(score)
            return score
        elif len(counter) == 1:
            commonest = commonest[0][0]
            if commonest == 1:
                score += 4000
                print(score)
                return score
            else:
                score += commonest * 400
                print(score)
                return score
        elif len(counter) == 3 and commonest[0][1] == 2:
            score += 1500
            print(score)
            return score
        elif len(counter) == 2 and commonest[0][1] == 3:
            if commonest[0][0] == 1:
                score += 1000
            else:
                score += commonest[0][0] * 100

            if commonest[1][0] == 1:
                score += 1000
            else:
                score += commonest[1][0] * 100

            print(score)
            return score


if __name__ == "__main__":
    new_game = GameLogic()

    new_game.calculate_score((2, 2, 2, 1, 1, 1))
