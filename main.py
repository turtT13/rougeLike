import random
import pygame
import os
from levels import Level_Gen

print("hello World")

WIDTH, HEIGHT = 768, 768
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("drogen")
VEL = 1
FPS = 60
TILE_SIZE = 64
walls = [pygame.image.load(os.path.join('imgs', 'walls', 'wall1.png')),
         pygame.image.load(os.path.join('imgs', 'walls', 'wall2.png')),
         pygame.image.load(os.path.join('imgs', 'walls', 'wall3.png')),
         pygame.image.load(os.path.join('imgs', 'walls', 'wall4.png'))]


WORLD_DATA = Level_Gen(random.randint(1,2))
WORLD_DATA = WORLD_DATA.getWorld()
PLAYER = pygame.image.load(os.path.join('imgs', 'player.png'))


class World():
    def __init__(self, data):

        self.tile_list = []

        wall1 = pygame.transform.scale2x(walls[0])
        wall2 = pygame.transform.scale2x(walls[1])
        wall3 = pygame.transform.scale2x(walls[2])
        wall4 = pygame.transform.scale2x(walls[3])

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    wall1_rect = wall1.get_rect()
                    wall1_rect.x = col_count*TILE_SIZE
                    wall1_rect.y = row_count*TILE_SIZE
                    tile = (wall1, wall1_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    wall2_rect = wall2.get_rect()
                    wall2_rect.x = col_count*TILE_SIZE
                    wall2_rect.y = row_count*TILE_SIZE
                    tile = (wall2, wall2_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    wall3_rect = wall3.get_rect()
                    wall3_rect.x = col_count*TILE_SIZE
                    wall3_rect.y = row_count*TILE_SIZE
                    tile = (wall3, wall3_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    wall4_rect = wall4.get_rect()
                    wall4_rect.x = col_count*TILE_SIZE
                    wall4_rect.y = row_count*TILE_SIZE
                    tile = (wall4, wall4_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            WINDOW.blit(tile[0], tile[1])


def draw_window(rect):
    WINDOW.fill((134, 78, 90))
    WORLD.draw()
    WINDOW.blit(PLAYER, (rect.x, rect.y))
    pygame.display.update()


def movement(key, rect):
    for tile in WORLD.tile_list:
        if key[pygame.K_w] and not tile[1].colliderect(rect.x, rect.y - VEL, rect.width, rect.height):
            rect.y -= VEL
        if key[pygame.K_a] and not tile[1].colliderect(rect.x - VEL, rect.y, rect.width, rect.height):
            rect.x -= VEL
        if key[pygame.K_s] and not tile[1].colliderect(rect.x, rect.y + VEL, rect.width, rect.height):
            rect.y += VEL
        if key[pygame.K_d] and not tile[1].colliderect(rect.x + VEL, rect.y, rect.width, rect.height):
            rect.x += VEL


WORLD = World(WORLD_DATA)


def main():
    player_rect = pygame.Rect(0, 0, 32, 32)
    row_count = 0
    for row in WORLD_DATA:
        col_count = 0
        for col in row:
            if col == 10:
                player_rect = pygame.Rect(
                    row_count*TILE_SIZE, col_count*TILE_SIZE, 32, 32)
            col_count += 1
        row_count += 1

    wall_rect = pygame.Rect(100, 100, 32, 32)
    clock = pygame.time.Clock()

    running = True
    while(running):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys_pressed = pygame.key.get_pressed()

        movement(keys_pressed, player_rect)
        draw_window(player_rect)

    pygame.quit()


if __name__ == "__main__":
    main()
