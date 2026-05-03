import pygame
from constants import GRAVITY, JUMP_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

# Checks: Is the player's bottom (y + size) inside the platform's top (platform.y) to bottom (platform.y + platform.height)?
#Is the player horizontally overlapping the platform?
#Is the player moving downward (velocity_y > 0)?
#If all three: land on it. Same as the floor — clamp y, zero velocity_y, set on_ground = True.

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))