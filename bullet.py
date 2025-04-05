import pygame
from circleshape import CircleShape
from constants import BULLET_RADIUS

class Bullet(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,BULLET_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(
            surface = screen,
            color   = 'magenta',
            center  = self.position,
            radius  = self.radius,
            width   = 3
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation = (self.rotation * dt) % 360
