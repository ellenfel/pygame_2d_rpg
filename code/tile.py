import pygame
from settings import *
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, '../graphics/test/rock.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)