from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, ASTEROID_MIN_RADIUS 
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            for i in range(2):
                new_asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
                new_asteroid.velocity = self.velocity.rotate(10 * i)

