import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here


class Food(Actor):

    def __init__(self):
        '''
        Food class constructor. Inherits from Actor class.
        Sets the text and moves the food to different, random positions within
        the game board in the terminal.

        Args:
            self(Actor): an instance of Actor
        '''
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.reset()

    def get_points(self):
        '''
        Gets the points for when the snake gets the food.

        Args:
            self(Food): an instance of Food

        Returns:
            integer: The points each food is worth
        '''
        return self._points

    def reset(self):
        '''
        Resets the food, then moves to a random position within the game board
        in the terminal

        Args:
            self(Food): an instance of Food
        '''
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)
