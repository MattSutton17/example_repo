class Yatzy:

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return sum([d1, d2, d3, d4, d5])

    @staticmethod
    def yatzy(dice):
        return 50 if all(die == dice[0] for die in dice) else 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        return Yatzy.calculate_singles(rolls=[d1, d2, d3, d4, d5], value=1)

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        return Yatzy.calculate_singles(rolls=[d1, d2, d3, d4, d5], value=2)

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        return Yatzy.calculate_singles(rolls=[d1, d2, d3, d4, d5], value=3)

    def fours(self):
        return self.calculate_singles(self.dice, value=4)

    def fives(self):
        return self.calculate_singles(self.dice, value=5)

    def sixes(self):
        return self.calculate_singles(self.dice, value=6)

    @staticmethod
    def calculate_singles(rolls, value):
        return rolls.count(value) * value

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        rolls = [d1, d2, d3, d4, d5]

        for value in range(6, 0, -1):
            if rolls.count(value) == 2:
                return value * 2
        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        rolls = [d1, d2, d3, d4, d5]

        total = 0
        for value in range(6, 0, -1):
            if rolls.count(value) >= 2:
                total += value * 2
        return total if len(set(rolls)) <= 3 else 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if t[i] >= 3:
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
