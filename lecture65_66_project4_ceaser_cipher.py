alphabet =  ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

wanna_end = False
while not wanna_end:
     a = input("Type 'encrypt' for encryption,type 'decrypt' for decryption:")
     if a == 'encrypt':
            data = input("Type your message:\n")
            Data = data.lower()
            shift = int(input("Type the shift number:\n"))
            print("Here's the encrypted result:")
            Mas = " "
            for char in Data:
                if char in alphabet:
                   position = alphabet.index(char)
                   new_position = (position+shift)%26
                   Mas +=alphabet[new_position]
                else:
                    Mas +=char
            print(f"{Mas}")
            play_again = input(" Type 'yes' to continue and type 'no' to exit:")
            if play_again=='no':
                    wanna_end =True
                    print("Have a nice day,Bye")
     if a == 'decrypt':
            data = input("Type your message:\n")
            Data = data.lower()
            shift = int(input("Type the shift number:\n"))
            print("Here's the decrypted result:")
            Mas = " "
            for char in Data:
                if char in alphabet:
                     position = alphabet.index(char)
                     new_position = (position-shift)%26
                     Mas +=alphabet[new_position]
                else:
                    Mas+=char
            print(f"Here is the word : {Mas}")
            play_again = input(" Type 'yes' to continue and type 'no' to exit:")
            if play_again == 'no':
                      wanna_end = True
                      print("Have a nice day,Bye")

