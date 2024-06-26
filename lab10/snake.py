# Media files taken from "Snake III" game 

import pygame
import random
import time
import sys
import psycopg2
from threading import Timer

pygame.init()
    
# Window resolution (HD)
res = w, h = 700, 700

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Some variables
SPEED = 1
SCORE = 0
LEVEL = 0
x = 0

# Establish connection to the PostgreSQL database
conn = psycopg2.connect(database="mydatabase", user="postgres", password="nazyken13", host="localhost", port="5432")
cur = conn.cursor()
# Create tables for Snake
cur.execute('''CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL,
                score TEXT NOT NULL,
                level TEXT NOT NULL)''')

# Creating a green screen and caption of game
pygame.display.set_caption("SNAKE")
pygame.display.set_icon(pygame.image.load("/Users/nieyrinn/Desktop/PP2/lab10/snake/icon.png"))
DISPLAYSURF = pygame.display.set_mode((res))

startdirection = 'RIGHT'
direction = startdirection

#sanek
snake_pos = [50, 50]
snake_body = [[50, 50],[40, 50]]

# fruit
fruit = pygame.transform.scale(pygame.image.load("/Users/nieyrinn/Desktop/PP2/lab10/snake/food.png"), (20, 10))
fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit_spawn = True
# fruit2
fruit2 = pygame.transform.scale(pygame.image.load("/Users/nieyrinn/Desktop/PP2/lab10/snake/food2.png"), (20, 10))
fruit2_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit2_spawn = True
# fruit3
fruit3 = pygame.transform.scale(pygame.image.load("/Users/nieyrinn/Desktop/PP2/lab10/snake/food3.png"), (20, 10))
fruit3_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit3_spawn = True
# fruit4
fruit4 = pygame.transform.scale(pygame.image.load("/Users/nieyrinn/Desktop/PP2/lab10/snake/food4.png"), (20, 10))
fruit4_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
fruit4_spawn = True

def score(SCORE, LEVEL):
   
    font = pygame.font.SysFont("Verdana", 15)
     
    score_surface = font.render("Score : " + str(SCORE), True, BLACK)
    level_surface = font.render("Level : " + str(LEVEL), True, BLACK)
    
    score_rect = score_surface.get_rect()

    DISPLAYSURF.blit(score_surface, score_rect)
    DISPLAYSURF.blit(level_surface, (200, 0))

def win():
    DISPLAYSURF.fill(BLUE)
    font = pygame.font.SysFont("Verdana", 15)
    win_surface = font.render("You won! You are going to the level " + str(LEVEL), True, BLACK)
    win_rect = win_surface.get_rect()
    pygame.mixer.Sound("/Users/nieyrinn/Desktop/PP2/lab10/snake/win.mp3").play()
    DISPLAYSURF.blit(win_surface, win_rect)
    pygame.display.flip()

    time.sleep(6)
    DISPLAYSURF.fill(GREEN)

def game_over():
    DISPLAYSURF.fill(RED)
    font = pygame.font.SysFont("Verdana", 15)
    game_over_surface = font.render("You lost! Your Score is: " + str(SCORE), True, BLACK)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (w/2, h/3)
    
    pygame.mixer.Sound("/Users/nieyrinn/Desktop/PP2/lab10/snake/gameover.mp3").play()
    DISPLAYSURF.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(6)
    name = input("Enter you nickname to register you: ")
    cur.execute("SELECT * FROM players WHERE username = %s", (name,))
    players = cur.fetchall()
    print(players)
    if len(players) == 0:
        cur.execute("INSERT INTO players (username, score, level) VALUES (%s, %s, %s)", (name, SCORE, LEVEL))
    else:
        cur.execute("UPDATE players SET score = %s, level = %s WHERE username = %s", (SCORE, LEVEL, name))
    conn.commit()

    pygame.quit()
    sys.exit()

def killfood():
    fruit4_spawn = False

LIFETIME = Timer(10, killfood)
LIFETIME.start()

username = input("Enter your name: ")
cur.execute("SELECT * FROM players WHERE username = %s", (username,))
players = cur.fetchall()
print(players)
if len(players) == 0:
  	print("Sign up in the system after game")
else:
    print("Welcome back!")
    SCORE = int(players[0][2])
    LEVEL = int(players[0][3])

# Game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
    

    
    if direction == 'UP' and startdirection != 'DOWN':
        startdirection = 'UP'
    if direction == 'DOWN' and startdirection != 'UP':
        startdirection = 'DOWN'
    if direction == 'LEFT' and startdirection != 'RIGHT':
        startdirection = 'LEFT'
    if direction == 'RIGHT' and startdirection != 'LEFT':
        startdirection = 'RIGHT'

    
    if startdirection == 'UP':
        snake_pos[1] -= 10
    if startdirection == 'DOWN':
        snake_pos[1] += 10
    if startdirection == 'LEFT':
        snake_pos[0] -= 10
    if startdirection == 'RIGHT':
        snake_pos[0] += 10

    
    snake_body.insert(0, list(snake_pos))
    
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        SCORE += 1
        x+=1
        fruit_spawn = False
        pygame.mixer.Sound("/Users/nieyrinn/Desktop/PP2/lab10/snake/newfood.mp3").play()
    elif snake_pos[0] == fruit2_pos[0] and snake_pos[1] == fruit2_pos[1]:
        SCORE += 2
        x+=2
        fruit2_spawn = False
        pygame.mixer.Sound("/Users/nieyrinn/Desktop/PP2/lab10/snake/newfood.mp3").play()
    elif snake_pos[0] == fruit3_pos[0] and snake_pos[1] == fruit3_pos[1]:
        SCORE += 1
        x+=1
        fruit3_spawn = False
        pygame.mixer.Sound("/Users/nieyrinn/Desktop/PP2/lab10/snake/newfood.mp3").play()
    elif snake_pos[0] == fruit4_pos[0] and snake_pos[1] == fruit4_pos[1]:
        SCORE += 3
        x+=3
        fruit4_spawn = False
        LIFETIME = Timer(10, killfood)
        LIFETIME.start()
        pygame.mixer.Sound("/Users/nieyrinn/Desktop/PP2/lab10/snake/newfood.mp3").play()
    else:
        snake_body.pop()

    DISPLAYSURF.fill(GREEN)

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
    fruit_spawn = True	
    DISPLAYSURF.blit(fruit, (fruit_pos[0]-7.5, fruit_pos[1]-7.5))
    if not fruit2_spawn:
        fruit2_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
    fruit2_spawn = True	
    DISPLAYSURF.blit(fruit2, (fruit2_pos[0]-7.5, fruit2_pos[1]-7.5))
    if not fruit3_spawn:
        fruit3_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
    fruit3_spawn = True	
    DISPLAYSURF.blit(fruit3, (fruit3_pos[0]-7.5, fruit3_pos[1]-7.5))
    if not fruit4_spawn:
        fruit4_pos = [random.randrange(1, (w//10)) * 10, random.randrange(1, (h//10)) * 10]
    fruit4_spawn = True	
    DISPLAYSURF.blit(fruit4, (fruit4_pos[0]-7.5, fruit4_pos[1]-7.5))
    
    for pos in range(len(snake_body)):
        if pos == 0:
            pygame.draw.circle(DISPLAYSURF, RED, (snake_body[pos][0], snake_body[pos][1]), 7.5)
        else:
            pygame.draw.circle(DISPLAYSURF, BLUE, (snake_body[pos][0], snake_body[pos][1]), 7.5)

    # border
    if snake_pos[0] < 0 or snake_pos[0] > w-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > h-10:
        game_over()

    # 5 fruits => next level + increase speed
    if x>=5:
        SPEED=SPEED+(LEVEL*2)
        LEVEL+=1
        x=0
        win()
    score(SCORE, LEVEL)
    
    pygame.display.update()
    FramePerSec.tick(FPS)
