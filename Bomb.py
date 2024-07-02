import pygame

from Wall import Wall
from Box import Box
from gameConfig import *
class Bomb(pygame.sprite.Sprite):
    def __init__(self, place):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.x = place[0] - (place[0]%BLOCK_SIZE)+BLOCK_SIZE - BLOCK_SIZE/2
        self.y = place[1] - (place[1]%BLOCK_SIZE)+BLOCK_SIZE - BLOCK_SIZE/2
        self.rect.center = (self.x, self.y)
        self.activation_time = pygame.time.get_ticks()
        self.explodeX = pygame.sprite.Sprite()
        self.explodeY = pygame.sprite.Sprite()
        self.exploded = False
        self.explodeRender = True
        self.radius = 4

    def update(self):
        current_time = pygame.time.get_ticks() # Время текущего тика
        if current_time - self.activation_time > 3000 and not self.exploded:
            self.explodeX.image = pygame.Surface((BLOCK_SIZE+BLOCK_SIZE*self.radius, BLOCK_SIZE))
            self.explodeY.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE+BLOCK_SIZE*self.radius))
            self.explodeX.image.fill(RED)
            self.explodeY.image.fill(RED)
            self.explodeX.rect = self.explodeX.image.get_rect()
            self.explodeY.rect = self.explodeY.image.get_rect()
            self.explodeX.rect.center = self.rect.center
            self.explodeY.rect.center = self.rect.center
            x_collide = pygame.sprite.spritecollide(self.explodeX, all_sprites, False)
            y_collide = pygame.sprite.spritecollide(self.explodeY, all_sprites, False)
            for sprite in x_collide:
                if sprite.__class__ == Wall:
                    if sprite.rect.left == self.explodeX.rect.right - BLOCK_SIZE*self.radius/2:
                        self.explodeX.image = pygame.transform.scale(self.explodeX.image, (BLOCK_SIZE + BLOCK_SIZE*self.radius/2, BLOCK_SIZE))
                        self.explodeX.rect = self.explodeX.image.get_rect()
                        self.explodeX.rect.x = self.rect.left - BLOCK_SIZE-BLOCK_SIZE*self.radius/2
                        self.explodeX.rect.y = self.rect.y

            all_sprites.remove(self)
            all_sprites.add(self.explodeX, self.explodeY)
            x_collide = pygame.sprite.spritecollide(self.explodeX, all_sprites, False)
            y_collide = pygame.sprite.spritecollide(self.explodeY, all_sprites, False)
            for sprite in x_collide:
                if sprite.__class__ == Box:
                    all_sprites.remove(sprite)
                    walls.remove(sprite)
            for sprite in y_collide:
                if sprite.__class__ == Box:
                    all_sprites.remove(sprite)
                    walls.remove(sprite)
            self.exploded = True
        elif current_time - self.activation_time > 3500 and self.explodeRender:
            all_sprites.remove(self.explodeX, self.explodeY)
            self.explodeRender = False


