from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
         super().__init__(x, y, radius)
         self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        baby1_velocity = self.velocity.rotate(angle) * 1.2
        baby2_velocity = self.velocity.rotate(-1 * angle) * 1.2
        Asteroid(self.position.x, self.position.y, new_radius, baby1_velocity)
        Asteroid(self.position.x, self.position.y, new_radius, baby2_velocity)