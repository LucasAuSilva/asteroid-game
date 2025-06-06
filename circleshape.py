import pygame

class CircleShape(pygame.sprite.Sprite):
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: float

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        if self.radius + other.radius > distance:
            return True
        return False

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
