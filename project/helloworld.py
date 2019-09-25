import pygame
import time

from pygame import font

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (255, 100, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hello Becky')
clock = pygame.time.Clock()

background = pygame.image.load("background_image.png").convert()
background = pygame.transform.scale(background, (display_width, display_height))

success_background = pygame.image.load("success_image.png").convert()
success_background = pygame.transform.scale(success_background, (display_width, display_height))

earth = pygame.image.load("earth.png").convert()
earth = pygame.transform.scale(earth, (80, 80))

mars = pygame.image.load("mars.png").convert()
mars = pygame.transform.scale(mars, (80, 80))

neptune = pygame.image.load("Neptune.png").convert()
neptune = pygame.transform.scale(neptune, (80, 80))

mercury = pygame.image.load("mercury.png").convert()
mercury = pygame.transform.scale(mercury, (80, 80))



def quitgame():
    pygame.quit()


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Hello World Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))

        gameDisplay.blit(background, [0, 0])
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        # print(mouse)

        if 150 + 100 > mouse[0] > 150 and 350 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150, 350, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 350, 100, 50))

        if 550 + 100 > mouse[0] > 550 and 350 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (550, 350, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (550, 350, 100, 50))

        button("START", 150, 350, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 350, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(5)



def game_loop():

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 40)

        TextSurf, TextRect = text_objects("Can you find the right world?", largeText)
        TextRect.center = ((display_width / 2), (display_height / 8))

        gameDisplay.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

        # print(mouse)

        if 150 + 100 > mouse[0] > 150 and 150 + 100 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, black, (150, 150, 100, 100))
        else:
            pygame.draw.rect(gameDisplay, white, (150, 150, 100, 100))

        if 550 + 100 > mouse[0] > 550 and 400 + 100 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, black, (550, 400, 100, 100))
        else:
            pygame.draw.rect(gameDisplay, white, (550, 400, 100, 100))

        if 150 + 100 > mouse[0] > 150 and 400 + 100 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, black, (150, 400, 100, 100))
        else:
            pygame.draw.rect(gameDisplay, white, (150, 400, 100, 100))

        if 550 + 100 > mouse[0] > 550 and 150 + 100 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, black, (550, 150, 100, 100))
        else:
            pygame.draw.rect(gameDisplay, white, (550, 150, 100, 100))

        button("", 150, 150, 100, 100, white, black, success_loop)
        button("", 150, 400, 100, 100, white, black, game_intro)
        button("", 550, 150, 100, 100, white, black, game_intro)
        button("", 550, 400, 100, 100, white, black, game_intro)

        gameDisplay.blit(earth, [160, 160])
        gameDisplay.blit(mars, [560, 410])
        gameDisplay.blit(neptune, [160, 410])
        gameDisplay.blit(mercury, [560, 160])

        pygame.display.update()
        clock.tick(15)


def success_loop():

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(success_background, [0, 0])

        largeText = pygame.font.Font('freesansbold.ttf', 50)

        TextSurf, TextRect = text_objects("HELLO WORLD!", largeText)
        TextRect.center = ((display_width / 1.7), (display_height / 8))

        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 700 + 100 > mouse[0] > 550 and 550 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (700, 550, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (700, 550, 100, 50))

        button("Quit", 700, 550, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


game_intro()
game_loop()
pygame.quit()
quit()
