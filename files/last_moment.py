import pygame
import pygame.mixer
import time
# классы для конца игры
from files.end_play import *
# цвета
# yellow=(255,255,0)
# red=(255,0,0)
white=(255,255,255)
# blue=(0,0,255)
# green=(0,255,0)
black=(0,0,0)
def end(win):
    # оформление
    pygame.init()
    screen=pygame.display.set_mode((1300,800))
    pygame.display.set_caption("Игра престолов")
    score_font = pygame.font.SysFont("comicsansms", 35)
    # отрисовка картинок
    varis2=Varis2(screen)
    varis3=Varis3(screen)
    tyrion2=Tyrion2(screen)
    tyrion3=Tyrion3(screen)
    # 
    # часть 1
    start=time.time()
    if win==False:
        # воспроизведение музыки
        pygame.mixer.music.load("C:\\Users\\nicit\\Desktop\\игра\\музыка\\193e2427b377e45.mp3")
        pygame.mixer.music.play()
        ######
        while True:
            screen.fill(white)
            varis2.output()
            if (time.time()-start)>2.6:
                break
            value = score_font.render("Лорд Варис умер! ", True, black)
            screen.blit(value, [550, 0])
            # обновление экрана
            pygame.display.update()
        start=time.time()
        while True:
            screen.fill(white)
            tyrion2.output()
            if (time.time()-start)>2.6:
                break
            # обновление экрана
            pygame.display.update()        
    # часть 2
    elif win==True:
        # воспроизведение музыки
        pygame.mixer.music.load("C:\\Users\\nicit\\Desktop\\игра\\музыка\\e377e9b8d135e68.mp3")
        pygame.mixer.music.play()
        #########
        start=time.time()
        while True:
            screen.fill(white)
            varis3.output()
            if (time.time()-start)>2.6:
                break
            value = score_font.render("Лорд Варис победил! ", True, black)
            screen.blit(value, [450, 0])
            # # обновление экрана
            pygame.display.update()
        start=time.time()
        while True:
            screen.fill(white)
            tyrion3.output()
            if (time.time()-start)>2.6:
                break
            # обновление экрана
            pygame.display.update()  