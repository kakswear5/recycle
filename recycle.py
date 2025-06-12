
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
        screen.draw.text("Game Over",fontsize=60,center = CENTER, color="black")
        screen.draw.text("Try Again",fontsize=40,center = (CENTER_X, CENTER_Y+30),color="black")
    
    elif game_complete():
        screen.draw.text("Good Job ",fontsize=65,center = CENTER,color="black")
        screen.draw.text("You Did Well",fontsize=60,center = (CENTER_X, CENTER_Y+35),color="black")

    else:
        for item in items:
            item.draw()    

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create (number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
   



def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range (0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items (items_to_create):
    new_items=[]
    for i in items_to_create:
        item=Actor(i + "img")
        new_items.append(item)
    return new_items
 
def layout_items (items_to_layout):
    number_of_gaps= len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    for i , item in enumerate(items_to_layout):
        new_x_pos = (i + 1) * gap_size  
        item.x = new_x_pos 

def animate_items (items_to_animate):
    global animations
    for i in items_to_animate:
        dur=START_SPEED-current_level
        i.anchor=("center","bottom")
        animation=animate(i,duration=dur,on_finished= handle_game_over,y = HEIGHT)
        animations.append(animation)


def handle_game_over():
    global game_over 
    game_over=True

def on_mouse_down(pos):
    global items,current_level
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handle_game_complete()
            else: 
                handle_game_over()


def handle_game_complete():
    global items,animations,current_level,game_complete
    stop_animations
    if current_level == FINAL_LEVEL:
       handle_game_complete()
    else:
        current_level = current_level + 1
        items = []
        animations = [] 

def stop_animations(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()

pgzrun.go()
        
    