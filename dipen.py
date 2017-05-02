import pygame
import time
import random

pygame.init()

width = 800
height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_width = 100

block_color = [53,115,255] 


gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('My first Game?')
clock = pygame.time.Clock()

carImg = pygame.image.load("car.png")

def things_dodged(count):
    font = pygame.font.Font(None, 30)
    text = font.render("Dodged "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, block_color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def crash() :
    message_display("You Crashed")

def text_objects(text,font) :
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font(None,115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()


def game_loop():

    x = width*0.45
    y = height*0.8

    x_change = 0

    thing_startx = random.randrange(0, width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   x_change = 0
            
        x += x_change
                
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        
        car(x,y)
        things_dodged(dodged)

        if(x > width - car_width or x < 0):
            crash()

        if thing_starty > height :
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)


        if y < thing_starty + thing_height :
            # y crossover

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width :
                crash()
                
        pygame.display.update()

        clock.tick(60)
    
game_loop()
pygame.quit()
quit()
