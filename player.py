import pygame
from constants import GRAVITY, JUMP_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20

        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.on_ground = False

    def update(self, dt):
        self.on_ground = False
        if self.on_ground:
            self.velocity_y = 0.0
        else:
            self.velocity_y += GRAVITY * dt
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.size
            self.velocity_y = 0.0
            self.on_ground = True

    def move(self, direction):
        self.velocity_x = direction * 200

    def jump(self):
        if self.on_ground:
            self.velocity_y = -JUMP_SPEED
            self.on_ground = False
    
    def check_platform_collision(self, platform):
        if (self.y + self.size > platform.y and
            self.y < platform.y + platform.height and
            self.x + self.size > platform.x and
            self.x < platform.x + platform.width and
            self.velocity_y > 0):
            self.y = platform.y - self.size
            self.velocity_y = 0.0
            self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))
        