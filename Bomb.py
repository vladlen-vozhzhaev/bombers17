import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.center = self.player.rect.center
        self.activation_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks() # Время текущего тика
        deltaTime = current_time - self.activation_time
        if deltaTime < 3000:
            if deltaTime % 1000 < 500:
                self.image.fill((255,255,0))
            else:
                self.image.fill((255,0,0))

    #def activate(self):
