import random
import pygame

class Piece:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0

        self.display = display

        # self.randomize()

    def randomize(self):
        height = 500
        width = 500
        bumper = 30

        max_x = (height - bumper - 20)
        max_y = (height - bumper - 10)

        self.x_pos = random.randint(bumper, max_x)
        self.y_pos = random.randint(bumper, max_y)

    def draw(self):
        pygame.draw.rect(
            self.display,
            (255,255,0),
            [
                self.x_pos,
                self.y_pos,
                20,
                20
            ]
        )

