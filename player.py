import pygame
import random

class Player:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.speed = 5
        self.hunger = 100
        self.thirst = 100
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 255))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_s]: self.y += self.speed
        if keys[pygame.K_a]: self.x -= self.speed
        if keys[pygame.K_d]: self.x += self.speed
        self.hunger -= 0.02
        self.thirst -= 0.01

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))