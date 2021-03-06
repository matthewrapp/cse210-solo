from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction().scale(constants.PADDLE_MOVE_SCALE)
        paddle = cast["paddle"][0] # there's only one in the cast
        # paddle.change_y = direction.get_y()
        if paddle.center_x >= constants.MAX_X- paddle.width/2:
            paddle.center_x = constants.MAX_X - paddle.width/2 -1
            paddle.change_x = 0
        elif paddle.center_x <= 0+paddle.width/2:
            paddle.center_x = 1+paddle.width/2
            paddle.change_x = 0
        else: 
            paddle.change_x = direction.get_x()

