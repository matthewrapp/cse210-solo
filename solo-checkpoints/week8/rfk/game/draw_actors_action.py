from game.action import Action

# TODO: Define the DrawActorsAction class here


class DrawActorsAction(Action):

    def __init__(self, output_service):
        self.output_service = output_service

    def execute(self, cast):
        """
        Use the output_service attribute to draw the actors on the screen.
        Clear the screen, draw the actors, and then flush the buffer

        Args:
            cast (dict): the game actors
        """

        self.output_service.clear_screen()
        for group in cast.values():
            self.output_service.draw_actors(group)
        self.output_service.flush_buffer()
