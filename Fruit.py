from pygame.math import Vector2
CELL_SIZE = 40
NO_OF_CELLS = 20
BANNER_HEIGHT = 2
USER_SEED=76767
import random

random.seed(USER_SEED)


class Fruit:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.reset_seed()

    def generate_fruit(self):
        border = NO_OF_CELLS - 1

        x = random.randrange(1, border)
        y = random.randrange(BANNER_HEIGHT, border)
        self.position = Vector2(x, y)

    def reset_seed(self):
        random.seed(USER_SEED)
        self.generate_fruit()
