import random
print("Here we are going to play the Snake , Water and Gun game in which the person have to choice in given choices\n Here Snake beats the Water , Gun beats the Snake and Water beats the Water")
choices = ['s','g','w']
user_name = input("Will you give your fortunate name : ")
Chances = int(input(f"Mr./Ms. {user_name} , How many times do you want to play? => "))

score_of_user = 0
score_of_computer = 0

for i in range(0,Chances):
    user_input = input("Enter the first letter of your choice\n Eg:- s, g or w : ")
    computer_input = random.choice(choices)
    print("Choice of the Computer is "+ computer_input)
    if user_input == 's' and computer_input == 'w' :
        print(f"{user_name} is won this match")
        score_of_user= score_of_user + 1

    elif user_input == 's' and computer_input == 'g' :
        print(f"{user_name} is loss this match")
        score_of_computer= score_of_computer + 1

    elif user_input == 'w' and computer_input == 'g' :
        print(f"{user_name} is won this match")
        score_of_user= score_of_user + 1

    elif user_input == 'w' and computer_input == 's' :
        print(f"{user_name} is loss this match")
        score_of_computer= score_of_computer + 1

    elif user_input == 'g' and computer_input == 's' :
        print(f"{user_name} is won this match")
        score_of_user= score_of_user + 1

    elif user_input == 'g' and computer_input == 'w' :
        print(f"{user_name} is loss this match")
        score_of_computer= score_of_computer + 1

    else:
        print("This is the Draw")
        score_of_computer= score_of_computer + 1
        score_of_user= score_of_user + 1

print(f"Score of {user_name} is {score_of_user} out of {Chances}")