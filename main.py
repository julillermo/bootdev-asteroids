import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_time = pygame.time.Clock()
    dt = 0.0

    # Initialize player
    player = Player(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2,
    )

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for event in pygame.event.get():
            pass

        screen.fill(color="black")

        dt = clock_time.tick(60) / 1000

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
