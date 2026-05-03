import pygame
from player import Player
from game_platform import Platform

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Donkey Kong")

 #create a player instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

#create 3 platform instances
platform1 = Platform(100, 450, 200, 20)
platform2 = Platform(350, 350, 200, 20)
platform3 = Platform(500, 250, 200, 20)

#set up the clock for a decent framerate
clock = pygame.time.Clock()

#game loop
running = True
dt = 0.0
while running:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         keys = pygame.key.get_pressed()
         if keys[pygame.K_SPACE]:
             player.jump()

    
    player.update(dt) # Pass delta time in seconds
    
    player.check_platform_collision(platform1)
    player.check_platform_collision(platform2)
    player.check_platform_collision(platform3)
   
    #fill the screen with black
    screen.fill((0, 0, 0))
    
   
    player.draw(screen)
    platform1.draw(screen)
    platform2.draw(screen)
    platform3.draw(screen)

    #update the display
    pygame.display.flip()
    #cap the framerate at 60fps
    dt = clock.tick(60) / 1000.0 # Delta time in seconds

pygame.quit()