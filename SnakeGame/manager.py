import sys
import time
import keyboard
from snakeinfo import Snake
from snakeinfo import Board

New_Snake = Snake()
New_Board = Board(New_Snake.head, New_Snake.body, New_Snake.tail, New_Snake.food_object) 

New_Board.update_board()
print("Score: %s" % (New_Snake.score) + "  ", end = "")
print("Recommended size is 80 x 27")

speed = float(sys.argv[1])


def moving_up():
    New_Snake.move_up()
    New_Snake.food()
    New_Board.update_board()
    print("Score: %s" % (New_Snake.score))
    time.sleep(speed)

def moving_down():
    New_Snake.move_down()
    New_Snake.food()
    New_Board.update_board()
    print("Score: %s" % (New_Snake.score))
    time.sleep(speed)


def moving_left():
    New_Snake.move_left()
    New_Snake.food()
    New_Board.update_board()
    print("Score: %s" % (New_Snake.score))
    time.sleep(speed)

def moving_right():
    New_Snake.move_right()
    New_Snake.food()
    New_Board.update_board()
    print("Score: %s" % (New_Snake.score))
    time.sleep(speed)

pressed_key = None

while True :


    if keyboard.is_pressed('up arrow') :
        while True: 
            moving_up()
            if keyboard.is_pressed('down arrow') or keyboard.is_pressed('left arrow') or keyboard.is_pressed('right arrow') or New_Snake.dead == True:
                break
        
    if keyboard.is_pressed('down arrow'):
        while True:
            moving_down()
            if keyboard.is_pressed('up arrow') or keyboard.is_pressed('left arrow') or keyboard.is_pressed('right arrow') or New_Snake.dead == True:
                break
        
    if keyboard.is_pressed('left arrow'): 
        while True:
            moving_left()
            if keyboard.is_pressed('down arrow') or keyboard.is_pressed('up arrow') or keyboard.is_pressed('right arrow') or New_Snake.dead == True:
                break

    if keyboard.is_pressed('right arrow'):
        while True:
            moving_right()
            if keyboard.is_pressed('down arrow') or keyboard.is_pressed('left arrow') or keyboard.is_pressed('up arrow') or New_Snake.dead == True:
                break

    if New_Snake.dead == True:
        print("""
           /^\/^/
         _|__|  O|
\/     /~     \_/ /
 \____|__________/  /
        \_______      /
                `\     \                 /
                  |     |                  /
                 /      /                    /
                /     /                       \\
              /      /                         \ /
             /     /                            \  /
           /     /             _----_            \   /
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~

                                                         """)

        print("""
  ___                 
 / __|  __  ___  _ _    ___ 
 \__ \ / _ / _ \ | '_\ / -_)        %s
 |___/ \__ \___/ |_|   \___|      
             """ % (New_Snake.score))
                                
        break



