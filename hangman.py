import random
import hangmanstages
word_list=["apple","beautiful","potato","animal","puppy","doggy","salaar","hello","india"]
choosen_word=random.choice(word_list)
lives=6
display=[]
for i in range(len(choosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a Letter : ")
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("SORRY....You Lose The Game....!")
    if '_' not in display:
        game_over=True
        print("Whoo!!! You Won The Game......")
    print(hangmanstages.HANGMANPICS[lives])