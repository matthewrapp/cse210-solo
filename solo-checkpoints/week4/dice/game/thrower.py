import random


"""A code template for a person who is throwing the dice in the game. The responsibility of
    this class of objects is to keep track of the dice and the numbers that the dice show after a roll.

    Attributes:
        dice (List/Array INT): Keeps an array of 5 numbers. Each number is randomly generated 1-6
        pointsPerThrow (INT): Keeps tally of the amount of points in 1 throw
        pointsTotal (INT): Keeps a running total on all the throw
    """


class Thrower():
    def __init__(self, userName):
        self.userName = userName
        self.diceList = []
        self.numThrows = 0
        self.points = 0

    def throw_dice(self):
        self.diceList.clear()
        for number in range(0, 5):
            number = random.randint(1, 6)
            self.diceList.append(number)
        self.numThrows += 1

    def get_points(self):
        self.points = 0
        points = (self.diceList.count(1) * 100) + (self.diceList.count(5) * 50)
        return points

    def can_throw(self):
        return (self.diceList.count(1) > 0 or self.diceList.count(5) > 0 or self.numThrows == 0)


thrower1 = Thrower('Matthew')
print(thrower1)
