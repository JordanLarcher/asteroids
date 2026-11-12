from circleshape import CircleShape
import pygame
from pygame import Surface
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x:float, y:float, radius: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white",self.position, self.radius, SHOT_RADIUS )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt