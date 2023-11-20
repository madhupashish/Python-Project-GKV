import random
print("This is tic tac toe game , I'm assuming you know the rules already")
print("For the first person his sign is X and for the second person the sign is O")


def name():
    global player_names,x1,x2
    x1 = input("Enter first player name : ")
    x2 = input("Enter second player name : ")
    player_names = [x1,x2]

def choices():
    global Player_1, Player_2
    Player_1 = random.choice(player_names)
    if Player_1 == x1:
        global Player_2
        Player_2 = x2
    else:
        Player_2 = x1
    print(f"{Player_1} will go first")

def game_on():
    global count_player_1
    global count_player_2
    count_player_1 = 0
    count_player_2 = 0
    while True:
        global A  
        # List of number in pattern      
        A = ["1","2","3","4","5","6","7","8","9"]
        # Printing the pattern
        print(f"{A[0]}|{A[1]}|{A[2]}\n-----\n{A[3]}|{A[4]}|{A[5]}\n-----\n{A[6]}|{A[7]}|{A[8]}")
        while True:
            Display()
            print(f"{Player_1} choose anyone in the pattern and your character is X")
            input_1 = str(input("Enter the choice: "))
            for i in range(9):
                # Checking whether it is already filled or not
                if A[i] == "X" or A[i] == "O":
                    continue
                else:
                    # Checking whether it is available or not
                    if input_1 == A[i]:
                        A[int(input_1)-1] = "X"
                         
            if A[0]==A[1]==A[2] == "X" or A[0]==A[4]==A[8] == "X"or A[0]==A[3]==A[6] == "X"or A[2]==A[5]==A[8] == "X"or A[6]==A[7]==A[8] == "X"or A[1]==A[4]==A[7] == "X"or A[2]==A[4]==A[6] == "X":
                print(f"{Player_1} won !!!")
                count_player_1+=1
                break
                        
            Display()
            print(f"{Player_2} is your turn and your character is O")
            input_2 = str(input("Enter your choice: "))
            for j in range(9):
                if A[j] == "X" or A[j] == "O":
                    continue
                else:
                    if input_2 == A[j]:
                        A[int(input_2)-1] = "O"
                         
            if A[0]==A[1]==A[2]== "O" or A[0]==A[4]==A[8]== "O"or A[0]==A[3]==A[6]== "O"or A[2]==A[5]==A[8]== "O"or A[6]==A[7]==A[8]== "O"or A[1]==A[4]==A[7]== "O"or A[2]==A[4]==A[6]== "O" :
                print(f"{Player_2} won !!!")
                count_player_2+=1
                break
            # Condition whether it is full or not
            box = 0
            for k in range(9):
                if (A[k] == "X" or A[k] == "O"):
                    box+=1
            if (box == 9):
                print("Noone won")
                break
                        
                    

            
        continue_game = input("Whether do you want to continue or not \n If continue enter Yes otherwise No: ")

        if continue_game == "Yes" or continue_game == "yes":
            continue
        else:
            break
                

def Display():
    for i in range(9):
        if A[i]=="X" or A[i]=="O":
            continue
    print(f"{A[0]}|{A[1]}|{A[2]}\n-----\n{A[3]}|{A[4]}|{A[5]}\n-----\n{A[6]}|{A[7]}|{A[8]}")
        
    
def result():
    print(f"{Player_1} points is ",end="")
    print(f"{count_player_1}")
    print(f"{Player_2} points is ",end="")
    print(f"{count_player_2}")


# Name of the players  
name()
# Choosing which player goes first
choices()
# Game start here
game_on()
# Result of the game 
result()       








    
