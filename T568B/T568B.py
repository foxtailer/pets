import pygame
from pygame.locals import *
from sys import exit
import time
import random

pygame.init()
pygame.display.set_caption("T568B")

screen = pygame.display.set_mode((310, 581), 0, 32)
font = pygame.font.SysFont("arial", 20)
bg = pygame.image.load(r"./img/empty.jpg").convert()
orange_white = pygame.image.load(r"./img/0.jpg").convert()
orange = pygame.image.load(r"./img/1.jpg").convert()
green_white = pygame.image.load(r"./img/2.jpg").convert()
blue = pygame.image.load(r"./img/3.jpg").convert()
blue_white = pygame.image.load(r"./img/4.jpg").convert()
green = pygame.image.load(r"./img/5.jpg").convert()
brown_white = pygame.image.load(r"./img/6.jpg").convert()
brown = pygame.image.load(r"./img/7.jpg").convert()
shuffle = pygame.image.load(r"./img/shuffle.jpg").convert()
check = pygame.image.load(r"./img/check.jpg").convert()
right_ansver = pygame.image.load(r"./img/True.jpg").convert()
wrong_ansver = pygame.image.load(r"./img/False.jpg").convert()

positions = [(41, 185),(70, 185), (99, 185),(125, 185), (154, 185), (180, 185), (210, 185), (238, 185)]
answer_positions = [(0,0), (31,0), (62,0), (93,0), (124,0), (155,0), (186,0), (217,0), (248,0), (279,0)]
original_order = (orange_white, orange, green_white, blue, blue_white, green, brown_white, brown)
answers = []
randomize = list(original_order)
selector_position = 0
item_selected = False
check_is_redy = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN: 
            if event.key == K_LEFT and selector_position>0: 
                if item_selected:
                    randomize[selector_position],randomize[selector_position-1]=randomize[selector_position-1],randomize[selector_position] 
                selector_position -= 1
            elif event.key == K_RIGHT and selector_position<(len(positions)-1): 
                if item_selected:
                    randomize[selector_position],randomize[selector_position+1]=randomize[selector_position+1],randomize[selector_position]
                selector_position += 1

            elif event.key == K_RETURN:
                if item_selected:
                    item_selected = False
                else:
                    item_selected = True

    x, y = pygame.mouse.get_pos()
    
    screen.blit(bg, (0,31))
    
    shuffle_rect = Rect((0,531), (155,50))
    check_rect = Rect((155,531), (155,50))
    screen.blit(shuffle, (0,531))
    screen.blit(check, (155,531))

    if pygame.mouse.get_pressed()[0]:
        if shuffle_rect.collidepoint(x,y):
            random.shuffle(randomize)
            check_is_redy = True

        if check_rect.collidepoint(x,y) and check_is_redy:
            if len(answers) == 10:
                answers.clear()
            if tuple(randomize) == original_order:
                screen.blit(right_ansver, (answer_positions[len(answers)]))
                answers.append(1)
                check_is_redy = False
            else:
                screen.blit(wrong_ansver, (answer_positions[len(answers)]))
                answers.append(1)

    for i in range(len(positions)):
        screen.blit(randomize[i], positions[i])

    pygame.draw.circle(screen, (0,0,0), (positions[selector_position][0]+12,450), 10)

    pygame.display.update()
    time.sleep(0.1)