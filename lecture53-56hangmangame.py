import random
word_list =["apple","potato","given","tomato","banana","sarika"]
lives = 6
chosen_word = random.choice(word_list)
display = [ ]
for i in chosen_word:
    display+= "_"
print(display)
game_over = False
while not game_over:
     guessed_letter = input("Guess the letter:").lower()
     for i in range(len(chosen_word)):
         letter = chosen_word[i]
         if letter==guessed_letter:
            display[i]=guessed_letter
     print(display)
     if guessed_letter not in chosen_word:
       lives-=1
       print(f"You haves {lives} lives left")
       if lives ==0:
           game_over =True
           print("You lose")
     if "_" not in display:
         game_over = True
         print("You win")