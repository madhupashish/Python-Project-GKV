import random
 
rand = random.randint(1,100)

guesses = [0]
print("WELCOME TO 'GUESS THE NUMBER!'")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell youyou're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
print(int(rand))
while True:
    guess1 = int(input('Guess the number: '))

    if guess1 > 100 or guess1 < 1 :
        print("Out of bound")
        break

    if guess1 == int(rand):
        print("Your choice is correct")
        break

    elif guess1 + 10 <= int(rand) or guess1-10 >= int(rand):
        print("COLD")

    elif guess1-10 < int(rand) and guess1+10 >int(rand) :
        print("You're WARM")

    while True:

        guess2 = int(input("Guess the number: "))

        if guess2-5 <= guess1 and guess1 <= guess2+5:
            print("You're Warmer")
            guess1 = guess2
            
        elif guess1>guess2-5 and guess2+5<guess1:
            print("You're a Colder")
            guess1 = guess2
            
        if guess1 > 100 or guess1 < 1 :
            print("Out of bound")
            break

        if guess1 == int(rand):
            print("Your choice is correct")
            break

        elif guess1 + 10 < int(rand) and guess1-10 > int(rand):
            print("COLD")
            break

        elif guess1-10 <= int(rand) and guess1+10 >=int(rand) :
            print("You're WARM")
            break       




    
