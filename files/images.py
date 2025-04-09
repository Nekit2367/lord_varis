import pygame
import random
filename_varis="images\\варис.webp"
filename_arya="images\\арья.webp"
filename_bronn="images\\бронн черноводный.webp"
filename_axe="images\\топор.webp"
class basa(pygame.sprite.Sprite):
    def __init__(self,screen,filename,size):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.image=pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
    def output(self):
        self.screen.blit(self.image,self.rect)
    def speed_0(self):
        return self.speed
    def update(self):
        self.rect.centerx+=self.speed
    

# ЛОРД ВАРИС
class Varis(basa):
    def __init__(self,screen):
        super().__init__(screen,filename_varis,(90, 59))
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        self.mright=False
        self.mleft=False
        self.mtop=False
        self.mbottom=False 
        self.mpay=False 
    def update_varis(self):
        if self.mright and self.rect.right<self.screen_rect.right:
            self.rect.centerx +=2
        elif self.mleft and self.rect.left>self.screen_rect.left:
            self.rect.centerx =self.rect.centerx-2
        elif self.mtop and self.rect.top>self.screen_rect.top:
            self.rect.centery -=2
        elif self.mbottom and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery +=2
    def pay(self):
        self.mpay=False
    def money(self):
        return self.mpay

# АРЬЯ СТАРК
class Arya(basa):
    def __init__(self,screen):
        super().__init__(screen,filename_arya,(90, 55))
        self.rect.left=self.screen_rect.right
        self.rect.centery=random.randint(50,750)
        self.speed=(-1)
    def new_speed_0(self):
        self.speed-=0.1

# БРОНН ЧЕРНОВОДНЫЙ
class Bronn(basa):
    def __init__(self,screen):
        super().__init__(screen,filename_bronn,(65, 90))
        self.rect.right=self.screen_rect.left
        self.rect.centery=random.randint(50,750)
        self.speed=float(1)
    def new_speed_0(self):
        self.speed+=0.1
        
# топор
class Axe(basa):
    def __init__(self,screen,x_axe,y_axe):
        super().__init__(screen,filename_axe,(32, 32))
        self.rect.centerx=x_axe
        self.rect.centery=y_axe
