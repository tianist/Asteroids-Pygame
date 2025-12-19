import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, SHOT_RADIUS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), LINE_WIDTH)
        super().draw(screen)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, angle):
        self.rotation += angle

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:
            self.rotate(-PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        shot = Shot(self.position, SHOT_RADIUS) 
        shot.velocity = forward  