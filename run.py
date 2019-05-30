import pygame, time, random
from pygame.locals import *

pygame.init()

width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

car_width = 100

block_color = (53, 115, 255)
largeText = pygame.font.Font(None, 80)
mediumText = pygame.font.Font(None, 50)
smallText = pygame.font.Font(None, 35)

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Racing game')
clock = pygame.time.Clock()
FPS = 60

carImg = pygame.image.load("car.png")
pygame.display.set_icon(carImg)

def obstacle_dodged(count):
    font = pygame.font.Font(None, 30)
    text = font.render("Dodged " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def draw_obstacle(thingx, thingy, thingw, thingh, block_color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x, y))

def crash() :
    message_display("You Crashed")

def text_objects(text, font, text_color = black) :
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()

def text_to_screen(text, text_x, text_y, size = "large", color = black):
    if size == "large":
        t_size = largeText
    elif size == "medium":
        t_size = mediumText
    elif size == "small":
        t_size = smallText

    TextSurf, TextRect = text_objects(text, t_size, color)
    TextRect.center = (text_x, text_y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def message_display(text):
    text_to_screen(text, width / 2, height / 2 - 40)
    text_to_screen("Press ENTER to restart", width / 2, height / 2 + 40, "medium")

    pygame.display.update()
    time.sleep(2)

    restart_f = False
    while not restart_f:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    restart_f = True

        pygame.display.update()
        clock.tick(10)

    game_loop()


def game_intro():
    gameDisplay.fill(white)

    text_to_screen("Ready to Race!", width / 2, height / 2 - 40, "large", green)
    text_to_screen("The more obstacles you avoid", width / 2, height / 2 + 40, "medium")
    text_to_screen("the more you score", width / 2, height / 2 + 70, "medium")
    text_to_screen("Press ENTER to play", width / 2, height / 2 + 100, "small", blue)

    game_intro_f = True
    while game_intro_f:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    game_intro_f = False

        pygame.display.update()
        clock.tick(5)

def game_loop():

    x = width * 0.45
    y = height * 0.8


    obstacle_w = 100
    obstacle_h = 100

    x_change = 0

    obstacle_x = random.randrange(0, width - int(obstacle_w))
    obstacle_y = -600
    obstacle_speed = 7

    dodged = 0

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x_change = -5
                elif event.key == K_RIGHT:
                    x_change = 5
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                   x_change = 0

        x += x_change

        gameDisplay.fill(white)

        draw_obstacle(obstacle_x, obstacle_y, obstacle_w, obstacle_h, block_color)
        obstacle_y += obstacle_speed

        car(x, y)
        obstacle_dodged(dodged)

        # Crash with window boundary
        if(x > width - car_width or x < 0):
            crash()

        # Crash with obstacle
        if y < obstacle_y + obstacle_h:
            # y crossover
            if x > obstacle_x and x < obstacle_x + obstacle_w or x + car_width > obstacle_x and x + car_width < obstacle_x + obstacle_w:
                crash()

        # Get next obstacle, update obstacle speed
        if obstacle_y > height:
            obstacle_y = 0 - obstacle_h
            obstacle_x = random.randrange(0, width - int(obstacle_w))
            dodged += 1
            obstacle_speed += 0.5
            obstacle_w += (dodged * 1.2)

        pygame.display.update()

        clock.tick(FPS)

game_intro()
game_loop()
pygame.quit()
quit()