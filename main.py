from textwrap import fill

import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroid = AsteroidField()

    player = Player(x, y, PLAYER_RADIUS)
    updatable.add(player)
    drawable.add(player)
    print(player.position)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        fill("black")
        updatable.update(dt)
        for asteroides in asteroids:
            if asteroides.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroides in asteroids:
            for shot in shots:
                if shot.collides_with(asteroides):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroides.kill()
        for draw in drawable:
            draw.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)

    print(player.position)

if __name__ == "__main__":
    main()
