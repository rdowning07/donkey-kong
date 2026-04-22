import pygame
from constants import GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20

        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def update(self, dt):
        self.velocity_y += GRAVITY * dt
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.size
            self.velocity_y = 0.0
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))
        