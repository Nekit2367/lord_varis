import pygame
class Baylish1():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("картинки\\мизинец говорит1.jpg")
        self.image = pygame.transform.scale(self.image, (990, 690))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.left=self.screen_rect.left
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
class Varis1():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("C:\\Users\\nicit\\Desktop\\игра\\картинки\\варис говорит1.jpg")
        self.image = pygame.transform.scale(self.image, (660, 660))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.right=self.screen_rect.right
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
class Tyrion1():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("C:\\Users\\nicit\\Desktop\\игра\\картинки\\тирион пойман.jpg")
        self.image = pygame.transform.scale(self.image, (1300, 800))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
class Tywin1():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("C:\\Users\\nicit\\Desktop\\игра\\картинки\\тавйвин главный.webp")
        self.image = pygame.transform.scale(self.image, (1000, 700))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.right=self.screen_rect.right
        self.rect.bottom=self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)
