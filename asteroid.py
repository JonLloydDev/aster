import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface = screen,
            color   = 'cyan',
            center  = self.position,
            radius  = self.radius,
            width   = 2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            settings = (
                self.position.x,
                self.position.y,
                self.radius - ASTEROID_MIN_RADIUS
            )
            asterA = Asteroid(*settings)
            asterA.velocity = self.velocity.rotate(angle) * 1.2
            asterB = Asteroid(*settings)
            asterB.velocity = self.velocity.rotate(-angle) * 1.2
        
