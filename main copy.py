import pygame
from circleshape import *
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers =(updatable, drawable)
    # game loop
    while True:
        # allow user to close or quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # set screen color black
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()  # refresh the screen
        dt = clock.tick(60) / 1000

    # temporary text on screen
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()