import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((
    display_width, display_height))
pygame.display.set_caption('Tower Defence')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()


def draw_map(self, x, y):
    """Draws the map from planisphere.png"""
    
