# The predefined set of lucky cards is as follows:
# ● Ace of Spade
# ● Any Heart
# ● Queen of Diamond
# ● King of Diamond
# ● Any 7

print("You have to choose a card from the Deck of 52 cards \n You can choose like 4 of Hearts or Jack of Diamond etc. \n These are the some examples for your choice")

choice = input("Enter the name of Card : ")

if choice == "Ace of Spade":
    print("Lucky You!")

elif choice == "Queen of Diamond":
    print("Lucky You!")

elif choice == "King of Diamond":
    print("Lucky You!")


list_of_choice = choice.split(" ")

if list_of_choice[0] == '7' :
    print("Lucky You!")

elif list_of_choice[2] == 'Heart':
    print("Lucky You!")

else :
    print("Better luck Next time")
