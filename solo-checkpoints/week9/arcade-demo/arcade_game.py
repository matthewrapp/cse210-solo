# Basic arcade shooter

# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0

# Classes


class Welcome(arcade.Window):
    """Main welcome window
    """

    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw a blue circle
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
        )

        # draw a rectangle, from x to x & y to y
        arcade.draw_lrtb_rectangle_filled(400, 600, 120, 60, arcade.color.BLUE)


class SpaceShooter(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        # Sprite  === represent your player as well as the enemies, other objects, etc. 2D picture of a game object
        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
    """Get the game ready to play
        Populate your sprite lists
    """

    # Set the background color
    arcade.set_background_color(arcade.color.SKY_BLUE)

    # Set up the player
    self.player = arcade.Sprite("images/jet.png", SCALING)
    self.player.center_y = self.height / 2  # center the plane vertically
    self.player.left = 10
    self.all_sprites.append(self.player)

    # Spawn a new enemy every 0.25 seconds
    arcade.schedule(self.add_enemy, 0.25)

    # Spawn a new cloud every second
    arcade.schedule(self.add_cloud, 1.0)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new enemy sprite
        enemy = arcade.Sprite("images/missile.png", SCALING)

        # Set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)


# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    arcade.run()
