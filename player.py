import pygame
import random
from constants import GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT
#__init__: position x, y, size 20, velocity_x = 0.0, velocity_y = 0.0
# update(self, dt): apply gravity to velocity_y, then apply velocity to position, then floor check — if the player goes below SCREEN_HEIGHT, clamp y to SCREEN_HEIGHT and zero out velocity_y
# draw(self, screen): draw a white rectangle using pygame.draw.rect

ASTEROID_SPEED = 100

class Asteroid:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.size = 20
        self.radius = radius

        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def update(self, dt):
        self.velocity_y += GRAVITY * dt
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.velocity_y = 0.0
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))
        