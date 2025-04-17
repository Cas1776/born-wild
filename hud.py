import pygame

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self, screen, player):
        hunger_text = self.font.render(f"Hunger: {int(player.hunger)}", True, (255, 255, 255))
        thirst_text = self.font.render(f"Thirst: {int(player.thirst)}", True, (255, 255, 255))
        screen.blit(hunger_text, (10, 10))
        screen.blit(thirst_text, (10, 30))