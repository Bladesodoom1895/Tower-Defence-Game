import pygame

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgs = []
        self.health = 1
        self.path = []