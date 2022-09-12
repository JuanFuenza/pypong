import pygame
from random import randint
from settings import *

class Player():
    def __init__(self, key_up: pygame.key, key_down: pygame.key, x_pos: int):
        self.vel = 0
        self.acc = 0.5
        self.friction = 0.99
        self.max_speed = 25
        self.key_up = key_up
        self.key_down = key_down
        self.x_pos = x_pos
        self.y_pos = HEIGHT//2
        self.color = (randint(50, 255), randint(50, 255), randint(50, 255))
        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 120))
        self.rect.center = (self.x_pos, HEIGHT//2)

    def handle_keys(self):
        """
        Player movement
        Returns: None"""
        key = pygame.key.get_pressed()
        if key[self.key_up]:
            if self.vel > -self.max_speed:
                self.vel -= self.acc

        if key[self.key_down]:
            if self.vel < self.max_speed:
                self.vel += self.acc
        
        self.y_pos += self.vel
        self.vel *= self.friction

        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 120))


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        
    def collision(self):
        """
        Limits the movement within certain boundries
        Returns: None
        """
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vel *= -1
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel *= -1

    def update(self):
        self.handle_keys()
        self.collision()