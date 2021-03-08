from game.point import Point
from game import constants

import arcade


class Ball(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.BALL_IMAGE)

        self.center_x = x
        self.center_y = y

        self.change_x = constants.BALL_SPEED
        self.change_y = constants.BALL_SPEED

    def bounce_vertical(self):
        self.change_x *= -1
        self.change_y *= -1

    def bounce_horizontal(self):
        self.change_y *= -1

    # def collides_with_sprite(self, brick):
    #     self.change_x *= -1
    #     self.change_y *= -1
