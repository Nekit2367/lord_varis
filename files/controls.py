import pygame, sys
def events(varis):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    varis.mright=True
                elif event.key==pygame.K_a:
                    varis.mleft=True
                elif event.key==pygame.K_w:
                    varis.mtop=True
                elif event.key==pygame.K_s:
                    varis.mbottom=True
                elif event.key==pygame.K_z:
                    varis.mpay=True     
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_d:
                    varis.mright=False
                elif event.key==pygame.K_a:
                    varis.mleft=False
                elif event.key==pygame.K_w:
                    varis.mtop=False
                elif event.key==pygame.K_s:
                    varis.mbottom=False
