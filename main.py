
import pygame
import sys


from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # clock
    clock = pygame.time.Clock()
    dt = 0
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    asteroid_filed = AsteroidField()
    # initi
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    # Game looop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.colliding(shot):
                    shot.kill()
                    asteroid.split()


            if asteroid.colliding(player):
                print("Game over!")
                sys.exit()
                
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()