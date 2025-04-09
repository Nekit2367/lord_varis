import pygame
from files.controls import *
import random
import pygame.mixer
import time
# классы для игры
from files.images import *
# цвета
yellow=(255,255,0)
red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
brown=(255, 64, 64, 255)
grey=(128,128,128)
olive=(128,128,0)
purple=(128,0,128)
# функция вывода случайного местоположения
def random_number():
    return random.randint(50,750)
# функции для включения музыки
def mus_money():
    pygame.mixer.init()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("C:\\Users\\nicit\\Desktop\\игра\\музыка\\popolnenie-scheta-v-kompyuternoy-igre.mp3"))
def mus_kill():
    pygame.mixer.init()
    pygame.mixer.Channel(3).play(pygame.mixer.Sound("C:\\Users\\nicit\\Desktop\\игра\\музыка\\launch1.mp3"))    
def mus_axe():
    pygame.mixer.init()
    pygame.mixer.Channel(4).play(pygame.mixer.Sound("C:\\Users\\nicit\\Desktop\\игра\\музыка\\Звук приобретения предметов в виртуальной игре.mp3"))    

# ОСНОВНАЯ ЧАСТЬ
def run():
    # изначальный цвет первой монетки
    color=red
    # оформление
    pygame.init()
    screen=pygame.display.set_mode((1300,800))
    pygame.display.set_caption("Игра престолов")
    font_style = pygame.font.SysFont("bahnschrift", 30)
    score_font = pygame.font.SysFont("comicsansms", 15)
    # основная музыка
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("C:\\Users\\nicit\\Desktop\\игра\\музыка\\igra_prestolov_-_Glavnaya_zastavka_63864630.mp3"))
    # функции, отвечающие за табло
    def Your_score(score):
        value = score_font.render("Ваш счёт: " + str(score), True, yellow)
        screen.blit(value, [0, 0])
    def Your_power(score):
        value = score_font.render("Ваша сила: " + str(score), True, yellow)
        screen.blit(value, [0, 20])
    def Your_kill(score):
        value = score_font.render("Врагов убито: " + str(score), True, yellow)
        screen.blit(value, [0, 40])
    def Your_time(score):
        value = score_font.render("Время игры: " + str(score), True, yellow)
        screen.blit(value, [0, 60])
    def Your_record(score):
        value = font_style.render("Рекорд: " + str(score), True, red)
        screen.blit(value, [500, 0])
    # победа/поражение вариса
    win=False
    # редкость появление топора
    random_number_axe=random.randint(2500,4500)
    # начальные координаты топора
    x_axe=random_number()
    y_axe=random_number()
    # создание вариса
    varis=Varis(screen)
    # создание массивов ообьектов
    massive_arya=pygame.sprite.Group()
    massive_bronn=pygame.sprite.Group()
    massive_axes=pygame.sprite.Group()
    # счетчики для обьектов
    count_arya=0
    count_bronn=0
    count_axe=0
    count_speed=0
    # счетчики для табло
    count=0
    power=0
    kill_person=0
    start=time.time()
    # переменная,отвечающая за окончание игры
    game_over=False
    # начальные координаты монетки
    x_money=random_number()
    y_money=random_number()
    # считываем предыдущий рекорд
    file=open("C:\\Users\\nicit\\Desktop\\игра\\файлы проги\\record.txt",'r')
    record=file.read()
    file.close()

    # основной цикл
    while True:  
        # управление и данные вариса  
        controls.events(varis)
        varis.update_varis()
        # цвет экрана
        screen.fill(blue)
        # покупка силы за монеты
        if varis.money()==True and count>=6:
            power+=1
            count-=6
        # создание врагов(арий)
        if count_arya>700:
            arya=Arya(screen)
            count_arya=0
            k=int(count_speed//1000)
            for i in range(k):
                arya.new_speed_0()
            massive_arya.add(arya)
        # создание врагов(броннов)
        if count_bronn>1000:
            bronn=Bronn(screen)
            count_bronn=0
            n=int(count_speed//1000)
            for i in range(n):
                bronn.new_speed_0()
            massive_bronn.add(bronn)
        
        # переберем всех арий
        collisions = pygame.sprite.spritecollide(varis,massive_arya , True)
        if collisions:
            if power==0:
                game_over=True
            else:
                power-=1
                mus_kill()
                kill_person+=1
        massive_arya.update()
        massive_arya.draw(screen)
        for sprite in massive_arya:
            if sprite.rect.right<0:
                massive_bronn.remove(sprite)
        # переберем всех броннов
        collisions = pygame.sprite.spritecollide(varis,massive_bronn , True)
        if collisions:
            if power==0:
                game_over=True
            else:
                power-=1
                mus_kill()
                kill_person+=1
        massive_bronn.update()
        massive_bronn.draw(screen)
        for sprite in massive_bronn:
            if sprite.rect.left>1300:
                massive_bronn.remove(sprite)
        # создание топориков
        if count_axe>random_number_axe:
            axe=Axe(screen,x_axe,y_axe)
            massive_axes.add(axe)
            count_axe=0
        # перебераем топорики
        p=0
        collisions=pygame.sprite.spritecollide(varis,massive_axes,True)
        if collisions:
            x_axe=random_number()
            y_axe=random_number()
            random_number_axe=random.randint(2500,4500)
            massive_axes.remove(sprite)
            p=1
        if p==1:
            mus_axe()
            power+=1
            p=0
        massive_axes.draw(screen)

        # обновленение позиции вариса
        varis.output()
        # обновление счетчиков
        count_arya+=1
        count_bronn+=1
        count_axe+=1
        count_speed+=0.2
        # сбор и рисовка монеты
        if x_money<varis.rect.right and x_money>varis.rect.left and y_money<varis.rect.bottom and y_money>varis.rect.top:
            count+=1
            x_money=random_number()
            y_money=random_number()
            mus_money()
            color=random.choice((red,yellow,brown,green,white,grey,olive,purple,yellow,white,green))
        pygame.draw.circle(screen,color,(x_money,y_money),15)

        # вывод табло
        time_play=time.time()-start
        Your_score(count)
        Your_power(power)
        Your_time(round(time_play))
        Your_kill(kill_person)
        Your_record(record)
        # покупа силы
        varis.pay()  
        # обновление экрана
        pygame.display.update()
        #проверка на окончание игры
        if game_over==True or time_play>120:
            win=True
            break
    # записываем новый рекорд
    if kill_person>int(record):
        record=kill_person
    file=open("C:\\Users\\nicit\\Desktop\\игра\\файлы проги\\record.txt",'w')
    file.write(str(record))
    file.close()
    # остановка музыки
    pygame.mixer.Channel(0).stop()
    # задержка экрана
    pygame.time.delay(300)
    return win