import random
import os
import sys
#draw grid
#pick a random location for the player
#pick random location for the exit door
#pick random location for the monster
#draw a player in the grid
#take input or movement
#move player,unless move(past edges of grid)
#check for win/lose
#clear screen and random grid

cells=[
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4)
]


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def get_location():
    return random.sample(cells,3)



def move_player(player,move):
    x,y=player

    if(move=="LEFT"):
        x-=1
    if(move=="RIGHT"):
        x+=1
    if(move=="UP"):
        y-=1
    if(move=="DOWN"):
        y+=1

    return x,y

def get_move(player):
    moves = {"LEFT","RIGHT","UP","DOWN"}
    x,y=player
    if (x==0):
        moves.remove("LEFT")
    if (x==4):
        moves.remove("RIGHT")
    if (y==0):
        moves.remove("UP")
    if (y==4):
        moves.remove("DOWN")
    return moves

def draw_map(player,door,monster):
    print(' _'*5)
    tile="|{}"

    for cell in cells:
        x,y=cell
        if(x<4):
            line_end=""
            if(cell==player):
                output=tile.format("x")
            elif(cell==door):
                output=tile.format("^")
            elif(cell==monster):
                output=tile.format("#")
            else:
                output=tile.format("_")
        else:
            line_end="\n"
            if(cell==player):
                output=tile.format("x|")
            else:
                output=tile.format("_|")
        print(output,end = line_end)


def game_loop():
    monster,door,player=get_location()
    playing=True
    while playing:
        clear_screen()
        draw_map(player,door,monster)
        valid_moves=get_move(player)
        print("you are currently in room {} ".format(player))
        print("You can move {} ".format(",".join(valid_moves)) )
        print("enter quit to exit")

        move=input(">")
        move=move.upper()

        if(move=="QUIT"):
            break
        if(move in valid_moves):
            player= move_player(player,move)
            if(player==monster):
                print("\n""Oh No ! The Monster got you""\n")
                playing=False
            if(player==door):
                print("\n""Congratulations !! You Did It""\n")
                playing=False
        else:
            input("\n**Walls Are hard! don't run into then **\n")
            
    else:
        if input("play again ? [Y/N]").lower() !="n" :
            game_loop()




clear_screen()
print("Welcome to the game")
input("press 'return' to start ! ")
clear_screen()
game_loop()

