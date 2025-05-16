import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Shot.containers = (updatables, drawables, shoots)
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                exit(0)

        screen.fill(color="black")
        for dw in drawables:
            dw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # miliseconds to seconds

if __name__ == "__main__":
    main()
