# Formations:

# Formation 1:
# ▣
# ▣
# ▣

# Formation 2:
# ▣ ▣ ▣

# Formation 3:
# ▣ ▣
#   ▣

# Formation 4:
# ▣ ▣
# ▣

# Formation 5:
#   ▣
# ▣ ▣

# Formation 6:
# ▣
# ▣ ▣


class Snake (object):

    def __init__(self):
        self.head = [3, 3]
        self.body = [3, 4]
        self.tail = [3, 5]

        self.last_move = "left"
        

    def move_up(self):

        if self.at_edge() == "at top edge":
            self.kill_screen()

        elif self.last_move == "down":
            self.invalid_move()
        
        elif self.check_formation() == "Formation 1: Head is Top":
            self.head[0] -= 1
            self.body[0] -= 1
            self.tail[0] -= 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 2: Head is Left":
            self.head[0] -= 1

            self.body[1] -= 1
            self.tail[1] -= 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 2: Head is Right":
            self.head[0] -= 1

            self.body[1] += 1
            self.tail[1] += 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 3: Head is Left":
            self.head[0] -= 1  
            self.tail[0] -= 1

            self.body[1] -= 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 4: Head is Right":
            self.head[0] -= 1
            self.tail[0] -= 1

            self.body[1] += 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 5: Head is Left":
            self.head[0] -= 1
            self.tail[0] += 1

            self.body[1] -= 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 5: Head is Up":
            self.head[0] -= 1
            self.body[0] -= 1
            
            self.tail[1] += 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 6: Head is Right":
            self.head[0] -= 1
            self.tail[0] += 1

            self.body[1] += 1
            self.last_move = "up"

        elif self.check_formation() == "Formation 6: Head is Up":
            self.head[0] -= 1
            self.body[0] -= 1

            self.tail[1] -= 1
            self.last_move = "up"


    def move_down(self):
        
        if self.at_edge() == "at bottom edge":
            self.kill_screen()
        
        elif self.last_move == "up":
            self.invalid_move()
            

        elif self.check_formation() == "Formation 1: Head is Bottom":
            self.head[0] += 1
            self.body[0] += 1
            self.tail[0] += 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 2: Head is Left":
            self.head[0] += 1

            self.body[1] -= 1
            self.tail[1] -= 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 2: Head is Right":
            self.head[0] += 1

            self.body[1] += 1
            self.tail[1] += 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 3: Head is Left":
            self.head[0] += 1
            self.tail[0] -= 1

            self.body[1] -= 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 3: Head is Down":
            self.head[0] += 1
            self.body[0] += 1

            self.tail[1] += 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 4: Head is Down":
            self.head[0] += 1
            self.body[0] += 1

            self.tail[1] -= 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 4: Head is Right":
            self.head[0] += 1
            self.tail[0] -= 1

            self.body[1] += 1
            self.last_move = "down"

        elif self.check_formation() == "Formation 5: Head is Left":
            self.head[0] += 1
            self.tail[0] += 1

            self.body[1] -= 1
            self.last_move = "down"
        
        elif self.check_formation() == "Formation 6: Head is Right":
            self.head[0] += 1
            self.tail[0] += 1

            self.body[1] += 1
            self.last_move = "down"

        

    
    def move_right(self):

        print(self.check_formation())

        if self.at_edge() == "at right edge":
            self.kill_screen()

        elif self.last_move == "left":
            self.invalid_move()

        elif self.check_formation() == "Formation 1: Head is Top":
            self.body[0] -= 1
            self.tail[0] -= 1

            self.head[1] += 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 1: Head is Bottom":
            self.body[0] += 1
            self.tail[0] += 1

            self.head[1] += 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 2: Head is Right":
            self.head[1] += 1
            self.body[1] += 1
            self.tail[1] += 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 3: Head is Down":
            self.body[0] += 1

            self.head[1] += 1
            self.tail[1] += 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 4: Head is Down":
            self.body[0] += 1

            self.head[1] += 1
            self.tail[1] -= 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 4: Head is Right":
            self.tail[0] -= 1

            self.head[1] += 1
            self.body[1] += 1
            self.last_move = "right"
        
        elif self.check_formation() == "Formation 5: Head is Up":
            self.body[0] -= 1

            self.head[1] += 1
            self.tail[1] += 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 6: Head is Up":
            self.body[0] -= 1

            self.head[1] += 1
            self.tail[1] -= 1
            self.last_move = "right"

        elif self.check_formation() == "Formation 6: Head is Right":
            self.tail[0] += 1

            self.head[1] += 1
            self.body[1] += 1
            self.last_move = "right"

    def move_left(self): 

        if self.at_edge() == "at left edge":
            self.kill_screen()

        elif self.last_move == "right":
            self.invalid_move()

        elif self.check_formation() == "Formation 1: Head is Top":
            self.body[0] -= 1
            self.tail[0] -= 1
            
            self.head[1] -= 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 1: Head is Bottom":
            self.body[0] += 1
            self.tail[0] += 1

            self.head[1] -= 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 2: Head is Left":
            self.head[1] -= 1
            self.body[1] -= 1
            self.tail[1] -= 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 3: Head is Left":
            self.tail[0] -= 1

            self.head[1] -= 1
            self.body[1] -= 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 3: Head is Down":
            self.body[0] += 1

            self.head[1] -= 1
            self.tail[1] += 1
            self.last_move = "left"
        
        elif self.check_formation() == "Formation 4: Head is Down":
            self.body[0] += 1

            self.head[1] -= 1
            self.tail[1] -= 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 5: Head is Up":
            self.body[0] -= 1

            self.head[1] -= 1
            self.tail[1] += 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 5: Head is Left":
            self.tail[0] += 1

            self.head[1] -= 1
            self.body[1] -= 1
            self.last_move = "left"

        elif self.check_formation() == "Formation 6: Head is Up":
            self.body[0] -= 1

            self.head[1] -= 1
            self.tail[1] -= 1


            self.last_move = "left"

        
     
    def at_edge(self):
        if self.head[0] == 1:
            return "at top edge" 
        
        if self.head[0] == 7:
            return "at bottom edge" 

        if self.head[1] == 1:
            return "at right edge" 

        if self.head[1] == 7:
            return "at left edge" 

    def check_formation(self):
        if self.head[1] == self.body[1] and self.body[1] == self.tail[1] and self.tail[1] == self.head[1] and self.head[0] + 1 == self.body[0] and self.body[0] + 1 == self.tail[0] and self.head[0] + 2 == self.tail[0]:
            return "Formation 1: Head is Top"

        elif self.head[1] == self.body[1] and self.body[1] == self.tail[1] and self.tail[1] == self.head[1] and self.head[0] - 1 == self.body[0] and self.body[0] - 1 == self.tail[0] and self.head[0] - 2 == self.tail[0]:
            return "Formation 1: Head is Bottom"

        elif self.head[0] == self.body[0] and self.body[0] == self.tail[0] and self.tail[0] == self.head[0] and self.head[1] + 1 == self.body[1] and self.body[1] + 1 == self.tail[1] and self.head[1] + 2 == self.tail[1]:
            return "Formation 2: Head is Left"

        elif self.head[0] == self.body[0] and self.body[0] == self.tail[0] and self.tail[0] == self.head[0] and self.head[1] - 1 == self.body[1] and self.body[1] - 1 == self.tail[1] and self.head[1] - 2 == self.tail[1]:
            return "Formation 2: Head is Right"

        elif self.head[0] == self.body[0] and self.body[0] + 1 == self.tail[0] and self.head[0] + 1 == self.tail[0] and self.head[1] + 1 == self.body[1] and self.body[1] == self.tail[1] and self.head[1] + 1 == self.tail[1]:
            return "Formation 3: Head is Left"

        elif self.head[0] - 1 == self.body[0] and self.body[0] == self.tail[0] and self.head[0] - 1 == self.tail[0] and self.head[1] == self.body[1] and self.body[1] - 1 == self.tail[1] and self.body[1] - 1 == self.tail[1]:
            return "Formation 3: Head is Down"

        elif self.head[0] == self.body[0] and self.body[0] + 1 == self.tail[0] and self.head[0] + 1 == self.tail[0] and self.head[1] - 1 == self.body[1] and self.body[1] == self.tail[1] and self.head[1] - 1 == self.tail[1]:
            return "Formation 4: Head is Right"
        
        elif self.head[0] - 1 == self.body[0] and self.body[0] == self.tail[0] and self.head[0] - 1 == self.tail[0] and self.head[1] == self.body[1] and self.body[1] + 1 == self.tail[1] and self.head[1] + 1 == self.tail[1]:
            return "Formation 4: Head is Down" 

        elif self.head[0] + 1 == self.body[0] and self.body[0] == self.tail[0] and self.head[0] + 1 == self.tail[0] and self.head[1] == self.body[1] and self.body[1] - 1 == self.tail[1] and self.head[1] - 1 == self.tail[1]:
            return "Formation 5: Head is Up"

        elif self.head[0] == self.body[0] and self.body[0] - 1 == self.tail[0] and self.head[0] - 1 == self.tail[0] and self.head[1] + 1 == self.body[1] and self.body[1] == self.tail[1] and self.head[1] + 1 == self.tail[1]:
            return "Formation 5: Head is Left"
        
        elif self.head[0] + 1 == self.body[0] and self.body[0] == self.tail[0] and self.head[0] + 1 == self.tail[0] and self.head[1] == self.body[1] and self.body[1] + 1 == self.tail[1] and self.head[1] + 1 == self.tail[1]:
            return "Formation 6: Head is Up"
        
        elif self.head[0] == self.body[0] and self.body[0] - 1 == self.tail[0] and self.head[0] - 1 == self.tail[0] and self.head[1] - 1 == self.body[1] and self.body[1] == self.tail[1] and self.head[1] - 1 == self.tail[1]:
            return "Formation 6: Head is Right"

    def kill_screen(self):
        print ("You are dead")

    def invalid_move(self):
        print ("You cannot move that way")

class Board (object):

    def __init__(self, head, body, tail):
        self.head = head
        self.body = body
        self.tail = tail

        self.game_board = [["▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"],
                      ["▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣"]]

    def update_board(self):

        split_1 = self.head
        self.game_board[split_1[0]][split_1[1]] = "□"
        
        split_2 = self.body
        self.game_board[split_2[0]][split_2[1]] = "□"

        split_3 = self.tail
        self.game_board[split_3[0]][split_3[1]] = "□"


        for x in self.game_board:
            print(x)

        self.game_board = [["▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"], 
                      ["▣", " ", " ", " ", " ", " ", " ", " ", "▣"],
                      ["▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣", "▣"]]
