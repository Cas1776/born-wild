import pygame
from core.player import Player
from core.hud import HUD

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.hud = HUD()
        self.font = pygame.font.SysFont("Arial", 24)

    def update(self):
        self.screen.fill((48, 77, 48))  # redwoods theme
        self.player.update()
        self.player.draw(self.screen)
        self.hud.draw(self.screen, self.player)
        self.draw_map_preview()

    def draw_map_preview(self):
        pygame.draw.circle(self.screen, (100, 200, 255), (400, 300), 200, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), (340, 300, 40, 40))  # Player 1
        pygame.draw.rect(self.screen, (255, 255, 255), (460, 300, 40, 40))  # Player 2
        text = self.font.render("Duel Arena Mockup", True, (255, 255, 0))
        self.screen.blit(text, (310, 270))