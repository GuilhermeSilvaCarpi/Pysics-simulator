import pygame

from body import Body
from player import Player
from stalker import Stalker
from time import time
from triangle import Triangle

# initializing
pygame.init()
display = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('an attempt at a game')
clock = pygame.time.Clock()
gameLoop = True
finalTime = time()-1
# game variables
buttons = [False, False, False, False]
# objects
player = Player(display)
player.shape.angle = 45

stalker = Stalker(display)
stalker.target = player
stalker.shape = Triangle([[0, 100], [50, 10], [100, 100]])

pen = Body(1, display)
pen.shape = Triangle([[0, 0], [2, - 200], [4, 0]])


# game loop
def update():
    player.update(buttons)
    stalker.update()
    pen.update()
    pen.pos = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]


def render():
    display.fill([10, 10, 10])

    for body in Body.group:
        body.render()

    pygame.display.update()


while gameLoop:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('game finished')
            gameLoop = False
            break
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            buttons[0] = True
        else:
            buttons[0] = False
        if pressed_keys[pygame.K_a]:
            buttons[1] = True
        else:
            buttons[1] = False
        if pressed_keys[pygame.K_s]:
            buttons[2] = True
        else:
            buttons[2] = False
        if pressed_keys[pygame.K_d]:
            buttons[3] = True
        else:
            buttons[3] = False
    # loop
    initialTime = finalTime
    finalTime = time()
    deltaTime = finalTime - initialTime

    Body.delta_time = deltaTime
    update()
    render()
    clock.tick(60)
