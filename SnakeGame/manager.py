import keyboard
from snakeinfo import Snake
from snakeinfo import Board

New_Snake = Snake()
New_Board = Board(New_Snake.head, New_Snake.body, New_Snake.tail) 

New_Board.update_board()
# print(New_Snake.check_formation())
move = input("Which way do you want to move? ") 

while True:

    # if keyboard.is_pressed('w'):
    if move == "up":
        New_Snake.move_up()
        New_Board.update_board()
        # print(New_Snake.check_formation())

    # if keyboard.is_pressed('s'):
    if move == "down":
        New_Snake.move_down()
        New_Board.update_board()
        # print(New_Snake.check_formation())

    # if keyboard.is_pressed('a'):    
    if move == "left":
        New_Snake.move_left()
        New_Board.update_board()
        # print(New_Snake.check_formation())

    # if keyboard.is_pressed('d'):
    if move == "right":
        New_Snake.move_right()
        New_Board.update_board()
        # print(New_Snake.check_formation())

    

    move = input("Which way do you want to move? ") 
