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
            return score

        elif len(counter) == 3 and commonest[0][1] == 2:
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
                    else:
                        pass
                elif item[1] == 1:
                    if item[0] == 1:
                        score += 100
                    elif item[0] == 5:
                        score += 50
                    else:
                        pass

            return score


if __name__ == "__main__":
    new_game = GameLogic()

    new_game.calculate_score((5,))
