import pygame
import pygame.mixer
import time
from files.dialog1 import *
# цвета
yellow=(255,255,0)
red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
def start():
    # оформление
    pygame.init()
    pygame.mixer.music.load("music\\c245b81d72ab0bb (1).mp3")
    pygame.mixer.music.play()
    screen=pygame.display.set_mode((1300,800))
    pygame.display.set_caption("Игра престолов")
    score_font = pygame.font.SysFont("comicsansms", 35)
    start=time.time()
    baylish1=Baylish1(screen)
    varis1=Varis1(screen)
    tyrion1=Tyrion1(screen)
    tywin1=Tywin1(screen)
    # часть 1
    while True:
        screen.fill(white)
        baylish1.output()
        if (time.time()-start)>2.8:
            break
        value = score_font.render("Лорд Варис, рад вас видеть! ", True, black)
        screen.blit(value, [0, 0])
        value = score_font.render("Что привело вас сюда? ", True, black)
        screen.blit(value, [0, 30])
        # обновление экрана
        pygame.display.update()

    # часть 2
    start=time.time()
    while True:
        screen.fill(white)
        varis1.output()
        if (time.time()-start)>2.8:
            break
        value = score_font.render("Лорд Бейлиш ", True, black)
        screen.blit(value, [650, 0])
        value = score_font.render("Мои пташки нашептали мне ", True, black)
        screen.blit(value, [650, 30])
        value = score_font.render("что мой старый друг в беде ", True, black)
        screen.blit(value, [650, 60])
        # обновление экрана
        pygame.display.update()
    # часть 3
    start=time.time()
    while True:
        screen.fill(white)
        baylish1.output()
        if (time.time()-start)>2.8:
            break
        value = score_font.render("Если я правильно понимаю вас, ", True, black)
        screen.blit(value, [0, 0])
        value = score_font.render("вы говорите о Тирионне ", True, black)
        screen.blit(value, [0, 30])
        value = score_font.render("Ланнистре", True, black)
        screen.blit(value, [0, 60])
        # обновление экрана
        pygame.display.update()
    # часть 4
    start=time.time()
    while True:
        screen.fill(white)
        varis1.output()
        if (time.time()-start)>2.8:
            break
        value = score_font.render("Тирионн Ланнистер сейчас обвинен", True, black)
        screen.blit(value, [650, 0])
        value = score_font.render("по несправедливым обвинениям", True, black)
        screen.blit(value, [650, 30])
        # обновление экрана
        pygame.display.update()
    # часть 5
    start=time.time()
    while True:
        screen.fill(white)
        baylish1.output()
        if (time.time()-start)>2.8:
            break
        value = score_font.render("Вы уверены, может спросим", True, black)
        screen.blit(value, [0, 0])
        value = score_font.render("одного нашего старого", True, black)
        screen.blit(value, [0, 30])
        value = score_font.render("знакомого", True, black)
        screen.blit(value, [0, 60])
        # обновление экрана
        pygame.display.update()
    # часть 6
    start=time.time()
    while True:
        screen.fill(white)
        varis1.output()
        if (time.time()-start)>2.8:
            break
        value = score_font.render("И кого же?", True, black)
        screen.blit(value, [650, 0])
        # обновление экрана
        pygame.display.update()
    # часть 7
    start=time.time()
    while True:
        screen.fill(white)
        tywin1.output()
        if (time.time()-start)>2.8:
            break
        # обновление экрана
        pygame.display.update()
    # часть 8
    start=time.time()
    while True:
        screen.fill(white)
        tyrion1.output()
        if (time.time()-start)>2.8:
            break
        # обновление экрана
        pygame.display.update()
    pygame.mixer.music.stop()