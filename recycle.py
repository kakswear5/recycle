
import pgzrun
import random


WIDTH = 800
HEIGHT = 650

CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

CENTER = (CENTER_X,CENTER_Y)

FINAL_LEVEL = 7

START_SPEED = 10 

ITEMS=["battery","bottle","chips","plastic"]

game_over = False

game_complete= False

current_level=1


items=[]
animations=[]

def draw():
    global game_over,game_complete,current_level,items
    screen.clear()
    screen.blit("bgimg",(0,0))

    if game_over():
        screen.draw.text("Game Over",fontsize=60,color=black,center=CENTER)



