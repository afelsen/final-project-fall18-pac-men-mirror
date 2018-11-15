import pygame

class Lives(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
