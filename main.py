import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers =(updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable, )
Shot.containers = (updatable, drawable, shots)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField() 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000
    

if __name__ == "__main__":
    main()
