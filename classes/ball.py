import pygame
from settings import *
from random import randint


class Ball():
    def __init__(self):
        self.vel_x = 5
        self.vel_y = 5
        self.acc = 0.5
        self.friction = 1
        self.max_speed = 25
        self.x_pos = WIDTH//2
        self.y_pos = HEIGHT//2
        self.color = (randint(50, 255), randint(50, 255), randint(50, 255))
        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 16))
        self.rect.center = (16, 120)

        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 16))

    def move(self):
        if self.rect.top <= 0 and self.vel_y < 0:
            self.rect.top = 0
            self.vel_y *= -1
        if self.rect.bottom >= HEIGHT and self.vel_y > 0:
            self.rect.bottom = HEIGHT
            self.vel_y *= -1

        self.x_pos += self.vel_x
        self.y_pos += self.vel_y
        self.vel_y *= self.friction
        self.vel_x *= self.friction

        self.rect = pygame.rect.Rect((int(self.x_pos), int(self.y_pos), 16, 16))
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.rect.center), 9)
    
    def update(self):
        self.move()