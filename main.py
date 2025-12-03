import pygame
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (drawable, updatable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")
    while True:
        log_state()
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collide_with(shot):
                    shot.kill()
                    asteroid.split()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for dra in drawable:
            dra.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
