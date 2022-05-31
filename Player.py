import os
import pygame
class Player:
    def __init__(self, world):
        self.img = pygame.image.load(os.path.join('imgs', 'player.png'))
        self.rect = self.img.get_rect()
        self.vel = 1
#----------gets starting position---------#
        row_count = 0
        for row in world:
            col_count = 0
            for col in row:
                if col == 10:
                    self.rect = pygame.Rect(
                        row_count*64, col_count*64, 32, 32)
                col_count += 1
            row_count += 1
    def get_rect(self):
        return self.rect
    def get_img(self):
        return self.img
    def movement(self, key):
        if key[pygame.K_w]:
            self.rect.y -= self.vel
        if key[pygame.K_a]:
            self.rect.x -= self.vel
        if key[pygame.K_s]:
            self.rect.y += self.vel
        if key[pygame.K_d]:
            self.rect.x += self.vel