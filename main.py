import pygame

from Bomb import Bomb
from Player import Player
from gameConfig import *
from Wall import Wall
pygame.init()

background_image = pygame.image.load("img/ground/ground_05.png")
background_width, background_height = background_image.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
walls = pygame.sprite.Group()
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 1:
            wall = Wall(50*j, 50*i)
            walls.add(wall)

player = Player(walls)
all_sprites.add(player, walls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
    if keys[pygame.K_SPACE]:
        bomb = Bomb(player)
        player.setBomb(bomb)

    player.update(dx, dy)
    for x in range(0, SCREEN_WIDTH, background_width):
        for y in range(0, SCREEN_HEIGHT, background_height):
            screen.blit(background_image, (x,y))

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)