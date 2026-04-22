import pygame
import player from Player

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Donkey Kong")

#set up the clock for a decent framerate
clock = pygame.time.Clock()

#game loop
running = True
while running:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #create a player instance
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    
    player.update(dt) # Pass delta time in seconds
    player.draw(screen)



    #fill the screen with black
    screen.fill((0, 0, 0))

    #update the display
    pygame.display.flip()
    #cap the framerate at 60fps
    dt = clock.tick(60) / 1000.0 # Delta time in seconds

pygame.quit()