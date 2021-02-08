import random

# TODO: Define the Board class here


class Board:

    def __init__(self):
        self._piles = []
        self._prepare()

    def apply(self, move):
        """
        Applies a move to the playing surface. In this case, meaning removing a number of stones from a pile

        Args:
        - self: an instance of Board()
        - move: an instance of Move()
        """
        # the pile the user wants to take from
        pile = move.get_pile()
        # the amount of stones the user wants to take from the pile
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)

    def is_empty(self):
        """
        Determines if all the stones have been removed from the board. Returns True if the board has no stones on it, false if otherwise

        Args:
        - self: an instance of Board()
        """
        empty = [0] * len(self._piles)
        return self._piles == empty

    def to_string(self):
        """
        Converts the board data to its string representation and returns it to the caller

        Args:
        - self: an isntance of Board()
        """
        text = "\n_____________________"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n____________________"
        return text

    def _prepare(self):
        """
        Sets up the board with a random number of piles (2-5) containing a random number of stones (1-9)

        Args:
        - self: an instance of Board()
        """
        pileRange = random.randint(2, 5)
        for pile in range(pileRange):
            stones = random.randint(1, 9)
            self._piles.append(stones)
