import pygame as py
import sys
from pygame.locals import *
import time

XO = 'x'
winner = None
draw = False
width = 500
height = 500
white = (255, 255, 255)
line_color = (10, 10, 10)

TTT = [[None]*10, [None]*10, [None]*10]
py.init()
fps = 60
Time = py.time.Clock()
screen = py.display.set_mode((width, height+100), 0, 32)
py.display.set_caption("Cờ caro")

opening = py.image.load('opening.jpeg')
x_img = py.image.load('x.png')
o_img = py.image.load('o.png')

x_img = py.transform.scale(x_img, (50, 50))
o_img = py.transform.scale(o_img, (50, 50))
opening = py.transform.scale(opening, (width, height))


def game_start():
    screen.blit(opening, (0, 0))
    py.display.update()
    time.sleep(1)
    screen.fill(white)

    py.draw.line(screen, line_color, (width/10, 0), (width/10, height), 7)
    py.draw.line(screen, line_color, (width / 10*2, 0), (width / 10*2, height), 7)

    py.draw.line(screen, line_color, (0, height/10), (width, height/10), 7)
    py.draw.line(screen, line_color, (0, height/10*2), (width, height/10*2), 7)
    game_status()


def game_status():
    global draw

    if winner is None:
        status = XO.upper() + "'s turn"
    else:
        status = winner.upper() + " won!"
    if draw:
        status = 'Draw!'

    font = py.font.Font(None, 40)
    text = font.render(status, 1, (255, 255, 255))

    screen.fill((0, 0, 0), (0, 500, 600, 100))
    status_rect = text.get_rect(center=(width/2, 600-50))
    screen.blit(text, status_rect)
    py.display.update()


    def check():
        global TTT, winner, draw

        for row in range (0,10)