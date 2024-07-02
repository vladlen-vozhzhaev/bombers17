import pygame
from gameConfig import *
class Bomb(pygame.sprite.Sprite):
    def __init__(self, place):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = place
        self.activation_time = pygame.time.get_ticks()
        self.explodeX = pygame.sprite.Sprite()
        self.explodeY = pygame.sprite.Sprite()
        self.exploded = False
        self.explodeRender = True

    def update(self):
        current_time = pygame.time.get_ticks() # Время текущего тика
        if current_time - self.activation_time > 3000 and not self.exploded:
            self.explodeX.image = pygame.Surface((BLOCK_SIZE+BLOCK_SIZE*2, BLOCK_SIZE))
            self.explodeY.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE+BLOCK_SIZE*2))
            self.explodeX.image.fill(RED)
            self.explodeY.image.fill(RED)
            self.explodeX.rect = self.explodeX.image.get_rect()
            self.explodeY.rect = self.explodeY.image.get_rect()
            self.explodeX.rect.center = self.rect.center
            self.explodeY.rect.center = self.rect.center
            all_sprites.remove(self)
            all_sprites.add(self.explodeX, self.explodeY)
            self.exploded = True
        elif current_time - self.activation_time > 3500 and self.explodeRender:
            all_sprites.remove(self.explodeX, self.explodeY)
            self.explodeRender = False


