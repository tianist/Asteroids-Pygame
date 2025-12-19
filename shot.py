from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = "white"
        self.WIDTH = LINE_WIDTH
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.WIDTH)
        