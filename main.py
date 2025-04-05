# Native

# Third-party
import pygame

# Local
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet


def main():
    print('Starting Asteroids!')
    pygame.init()

    running = True
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock   = pygame.time.Clock()
    dt      = 0

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets   = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.touching(bullet):
                    asteroid.split()
                    bullet.kill()

            if asteroid.touching(player):
                print('Game Over!')
                running = False
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
