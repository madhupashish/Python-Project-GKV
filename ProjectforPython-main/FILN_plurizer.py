# Converting singular noun into Plural
# Taking two input first one is non-negative integer and other one is string
# Here 1 is default case i.e., noun will not change if the input number is 1  
try:
    # Input Integer
    num_int = int(input("Enter the counting of your noun : "))
except:
    print("You entered a letter here, so please re run the program")
    exit(0)

# Here we inputing the singular noun
noun = input("Enter the noun which you want to convert into plural : ")

if num_int == 1:
    print(f"This is default case for 1 is {num_int} {noun}")

else:
    if noun[-2:] == 'fe':
        print(f"Plural of singular noun {noun} is {num_int} {noun[0:-2]+'ves'}")

    elif noun[-1] == 'y' and noun[-2]!='u' and noun[-2]!='o' and noun[-2]!='e' and noun[-2]!='a':
        print(f"Plural of singular noun {noun} is {num_int} {noun[:-1]+'ies'}")

    elif noun[-2:] == 'sh' or noun[-2:]=='ch':
        print(f"Plural of singular noun {noun} is {num_int} {noun +'es'}")

    elif noun[-2:] == 'us':
        print(f"Plural of singular noun {noun} is {num_int} {noun[:-2]+'i'}")

    elif noun[-2:] == 'ay' or noun[-2:] =='oy' or noun[-2:] =='ey' or noun[-2:] =='uy':
        print(f"Plural of singular noun {noun} is {num_int} {noun + 's'}")

    else:
        print(f"Plural of singular noun {noun} is {num_int} {noun + 's'}")