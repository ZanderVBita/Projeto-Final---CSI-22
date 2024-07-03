from AbstractCar import AbstractCar
import pygame
from utils import scale_image

RED_CAR = scale_image(pygame.image.load("Projeto-Final---CSI-22/imgs/red-car.png"), 0.55)

class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel / 2
        self.move()
