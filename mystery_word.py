import random
import operator
import os
import sys

words = open("words.txt", "r")
words_two = words.read()
word_bank = words_two.split()
guess_me = random.choice(word_bank)
breaker = list(guess_me)
str = ''
new_board = "_" * len(breaker)
scoreboard = list(new_board)
WRONG = []
past_guesses = []

def play_game():
    print(f"{str.join(scoreboard)} \n GUESS ME!")
    if len(WRONG) == 8:
        print(f"LOSER!\nThe Word Was: {guess_me}")
        sys.exit(0)
    if scoreboard == breaker:
        print("YOU WIN!")
        sys.exit(0)
    guess = input("Pick A Letter: ")
    if guess[0] in past_guesses:
        print("You Already Tried That...")
        play_game()
    elif guess[0] in breaker:
        print("good guess!")
        past_guesses.append(guess[0])
        guess_list = guess[0]
        for correct in range(len(breaker)):
            if breaker[correct] == guess_list:
                scoreboard[correct] = breaker[correct]
        play_game()
    elif guess[0] not in breaker:
        print("dumbass")
        past_guesses.append(guess[0])
        WRONG.append("X")
        print("X" * len(WRONG))
        play_game()





if __name__ == "__main__":
    play_game()
