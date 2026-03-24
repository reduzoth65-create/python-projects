import Pygame
Pygame.init()
screen=Pygame.display.set_mode((400,300))


while not done:
    for event in Pygame.event.get():
        if event.type==Pygame.QUIT:
            done=True
    Pygame.draw.rect(screen,(0,125,255),Pygame.Rect(30,30,60,60))

    Pygame.display.flip()