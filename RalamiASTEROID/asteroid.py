import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            newangle = random.uniform(20, 50)
            firstnewvector = self.velocity.rotate(newangle)
            secondnewvector = self.velocity.rotate(-newangle)
            splitasteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            splitasteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            splitasteroid1.velocity = firstnewvector * 1.2
            splitasteroid2.velocity = secondnewvector * 1.2
