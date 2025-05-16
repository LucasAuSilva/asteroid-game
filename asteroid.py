
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        _ = self.create_child_asteroid(random_angle)
        _ = self.create_child_asteroid(-random_angle)

    def create_child_asteroid(self, angle):
        vector = self.velocity.rotate(angle)
        new_radius = self.radius = ASTEROID_MIN_RADIUS
        child_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid.velocity = vector * 1.2
        return child_asteroid


