import pygame
import random
import time
import numpy as np
import gradient
import object
import motion

#all modules
pygame.init()

#game window
width = 500
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
score = 0

innercolor = [218, 251, 234]
outtercolor = [158, 250, 202]
name = 'image.jpg'
imgsize = (width, height)
gradient.circlegradient(innercolor, outtercolor, imgsize, name)
background_image = pygame.image.load("image.jpg").convert()

#snake
snake_color = (27, 154, 44)
snake_head = [250, 250] #center
snake_pstn = [[250, 250], [240, 250], [230, 250]] # blocks one by one , 1 is snake head
obj = object.Object()

img = pygame.image.load(r'C:\Users\dusia\PycharmProjects\Snake\aple.png')
apple_img = pygame.transform.scale(img, (20, 20))
apple_pstn = [random.randrange(1, 50)*10, random.randrange(1, 50)*10]

clock = pygame.time.Clock()

move = motion.Move()
action = object.Action()


def generate_snake(snake_head, snake_pstn, apple_pstn, btn_direction, score):

    if btn_direction == 1:
        snake_head[0] += 10
    elif btn_direction == 0:
        snake_head[0] -= 10
    elif btn_direction == 2:
        snake_head[1] += 10
    elif btn_direction == 3:
        snake_head[1] -= 10
    else :
        pass

    if (snake_head [0] >= apple_pstn[0] and snake_head[0] <= apple_pstn[0]+10) and \
            (snake_head[1] >= apple_pstn[1] and snake_head [1] <= apple_pstn [1]+10):
        apple_pstn, score = action.eat_apple(apple_pstn, score)
        snake_pstn.insert(0,list(snake_head))
    else:
        snake_pstn.insert(0, list(snake_head))
        snake_pstn.pop()

    return snake_pstn, apple_pstn, score

# final score


def display_final_score(display_text, final_score):
    largetext = pygame.font.Font('freesansbold.ttf',35)
    textS = largetext.render(display_text, True, snake_color)
    textR = textS.get_rect()
    textR.center = ((width/2), (height/2))
    pygame.display.update()
    time.sleep(2)


def blocked_direction(snake_pstn, current_direction_vector):
    next_step = snake_pstn[0]+current_direction_vector
    snake_head = snake_pstn[0]
    if move.collision_with_walls(snake_head) == 1 or move.collision_with_self(snake_pstn,snake_head):
        return 1
    else:
        return 0


def game(snake_head, snake_pstn, apple_pstn, btn_direction, apple, score):
    dead = False
    prev_btn_direction = 1
    btn_direction = 1
    current_direction_vector = np.array(snake_pstn[0])-np.array(snake_pstn[1])

    #window
    while dead is not True :
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                dead = True
            # directions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and prev_btn_direction != 1:  # !BACKWARD
                    btn_direction = 0
                elif event.key == pygame.K_RIGHT and prev_btn_direction != 0:
                    btn_direction = 1
                elif event.key == pygame.K_UP and prev_btn_direction != 2:
                    btn_direction = 3
                elif event.key == pygame.K_DOWN and prev_btn_direction != 3:
                    btn_direction = 2
                else:
                    btn_direction = btn_direction

        display.blit(background_image, [0, 0])
        obj.apple_display(apple_img, display, apple_pstn)
        obj.snake_display(snake_pstn, display, snake_color)

        snake_pstn, apple_pstn, score = generate_snake(snake_head, snake_pstn, apple_pstn, btn_direction, score)
        pygame.display.set_caption("Snake"+" "+"Score: "+str(score))
        pygame.display.update()
        prev_btn_direction = btn_direction
        if blocked_direction(snake_pstn,current_direction_vector) == 1:
            dead = True

        clock.tick(3)
    return 0


final_score = game(snake_head, snake_pstn, apple_pstn, 1, apple_img, score)

display = pygame.display.set_mode((width, height))
display.blit(background_image, [0, 0])
pygame.display.update()

display_text = 'Score: '+str(score)
display_final_score(display_text, final_score)

pygame.quit()