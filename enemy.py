import pygame

class Enemy:
    def __init__(self, x, y, imgs):
        self.x = x
        self.y = y
        self.imgs = []
        self.health = 1
        self.path = []