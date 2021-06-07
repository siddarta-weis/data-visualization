from random import randint

class Die():
    """ A class representing a die. """

    def __init__(self, num_sides=6) -> None:
        """ Assume a six-sided die. """
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
