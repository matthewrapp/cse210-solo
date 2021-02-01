import random

# TODO: Define the Rabbit class here


class Rabbit:
    """A code Template for the Rabit

    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Rabit (1-1000).
        distance (list): The distance traveled with each move.
    """

    def __init__(self):
        self.location = random.randint(1, 1000)
        # distance between the hunter and rabit
        self.distance = [0, 0]  # start with two so get_hint always works

    def get_hint(self):
        """Gets a message from the rabit.

        Args:
            self (Rabit): An instance of Rabit.

        Returns:
            string: A message from the rabit.
        """

        rabbitHint = "Can't find me! Hehe"
        if self.distance[-1] == 0:
            rabbitHint = 'You found me!'
        elif self.distance[-1] > self.distance[-2]:
            rabbitHint = 'Getting colder!'
        elif self.distance[-1] < self.distance[-2]:
            rabbitHint = 'Getting warmer!'
        return rabbitHint

    def watch(self, location):
        """Watches the location the the hunter and rabit and appends the difference 
        between the 2 locations into self.distance list.

        Args:
            self (Hunter): An instance of Rabit.
        """

        hunterLocation = location
        newDistance = abs(self.location - hunterLocation)
        self.distance.append(newDistance)
