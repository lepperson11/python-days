import random
from hangman_art import stages, logo
from hangman_words import word_list

word = random.choice(word_list )
placeholder = ""

correct = []
game = False
lives = 6
for i in word:
    placeholder += "_"
print(logo)
print(placeholder)
while game == False:
    guess = input("Guess a letter: ").lower()
    display = ""
    for i in word:
        if guess == i:
            display += guess
            correct.append(guess)
        elif i in correct:
            display += i
        else:
            display += "_"
    if word.find(guess) == -1:
        lives -= 1
        print(f"You Guessed {guess} That Was Not In The Word, You Lose A Life")
    
    print(display)
    print(f"****************************Lives Left: {lives}****************************")
    print(stages[lives])
    if lives == 0:
        print("***********************YOU LOSE**********************")
        print(f"The Correct Word Was: {word}")
        game = True
    if display == word:
        print("***********************YOU WIN**********************")
        game = True