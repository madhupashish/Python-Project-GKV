# Caesar Calipher code Project 1 from Aryan Sahu submitted to Mr. Namit Khanduja sir

def encryption(message,n):
    print(f"Your Plain text is : {message}")
    print(f"Shifting of text is {n}")
    print("Encrypted text is: ",end="")
    if message.isupper() == True:
        #Adding the message into the list
        words_upper = message.split(" ")
        for word in words_upper:
            list_letters1=[]
            for i in range(len(word)):
                e1 = ((ord(word[i])+n-65)%26+65)
                list_letters1.append(chr(e1))
            encrypted_code_upper = "".join(list_letters1)
            print(encrypted_code_upper,end=" ")

    elif message.islower() == True:
        #Adding the message into the list
        words_lower = message.split(" ")
        for word in words_lower:
            list_letters2 = []
            for i in range(len(word)):
                e2 = ((ord(word[i])+n-97)%26+97)
                list_letters2.append(chr(e2))
            encrypted_code_lower = "".join(list_letters2)
            print(encrypted_code_lower,end=" ")

    else:
        words = message.split(" ")
        for word in words:
            random_letter = []
            for i in range(len(word)):
                if word[i].isupper() == True:
                    e = ((ord(word[i])+n-65)%26+65)
                    random_letter.append(chr(e))

                elif word[i].islower()==True:
                    e = ((ord(word[i])+n-97)%26+97)
                    random_letter.append(chr(e))

            encrypted_code = "".join(random_letter)
            print(encrypted_code,end=" ")


def decryption(message,n):  
    print(f"Your Calipher text is : {message}")
    print(f"Shifting of text is {n}")
    print("Plain text is: ",end="")
    if message.isupper() == True:
        #Adding the message into the list
        words_upper = message.split(" ")
        for word in words_upper:
            list_letters1=[]
            for i in range(len(word)):
                e1 = ((ord(word[i])-n-65)%26+65)
                list_letters1.append(chr(e1))
            decrypted_code_upper = "".join(list_letters1)
            print(decrypted_code_upper,end=" ")

    elif message.islower() == True:
        #Adding the message into the list
        words_lower = message.split(" ")
        for word in words_lower:
            list_letters2 = []
            for i in range(len(word)):
                e2 = ((ord(word[i])-n-97)%26+97)
                list_letters2.append(chr(e2))
            decrypted_code_lower = "".join(list_letters2)
            print(decrypted_code_lower,end=" ")

    else:
        words = message.split(" ")
        for word in words:
            random_letter = []
            for i in range(len(word)):
                if word[i].isupper() == True:
                    e = ((ord(word[i])-n-65)%26+65)
                    random_letter.append(chr(e))

                elif word[i].islower()==True:
                    e = ((ord(word[i])-n-97)%26+97)
                    random_letter.append(chr(e))

            decrypted_code = "".join(random_letter)
            print(decrypted_code,end=" ")



message = input("Enter the message: ")
n = int(input("Enter the number of Shifting of letter: "))
print("Select 1 for encryption and 2 for decryption")
x = input("")

if x == "1":
    encryption(message,n)

else: 
    decryption(message,n)
