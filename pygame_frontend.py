import pygame

pygame.init()
screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
running = True

while running:
  clock.tick(60)
pygame.quit()
