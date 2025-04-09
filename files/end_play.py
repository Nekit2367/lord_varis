import pygame
class Varis2():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images\\варис умирает.jpg")
        self.image = pygame.transform.scale(self.image, (1000, 740))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.right=self.screen_rect.right
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)

class Varis3():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images\\варис победил.jpg")
        self.image = pygame.transform.scale(self.image, (980, 740))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
class Tyrion2():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images\\тирион проиграл.jpg")
        self.image = pygame.transform.scale(self.image, (1300, 800))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
class Tyrion3():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images\\тирион выиграл.webp")
        self.image = pygame.transform.scale(self.image, (1300, 800))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
