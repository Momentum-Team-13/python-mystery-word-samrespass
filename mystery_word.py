import random
import sys

words = open("words.txt", "r")
words_two = words.read()
word_bank = words_two.split()
guess_me = random.choice(word_bank)
breaker = list(guess_me)
str = ' '
new_board = "_" * len(breaker)
scoreboard = list(new_board)
WRONG = []
past_guesses = []

def play_game():
    if len(WRONG) == 8:
        print(f"LOSER!\nThe Word Was: {guess_me}")
        sys.exit(0)
    if scoreboard == breaker:
        print(f"{guess_me}\nYOU WIN!")
        sys.exit(0)
    else:
        print(f"{str.join(scoreboard)} \n GUESS ME!")
        guess = input("Pick A Letter: ").lower()
        if not guess.isalpha():
            print("Letters only!")
            play_game()
        elif len(guess) > 1:
            print("One at a time buddy.")
            play_game()
        elif guess in past_guesses:
            print("You Already Tried That...")
            play_game()
        elif guess in breaker:
            print("good guess!")
            past_guesses.append(guess)
            for correct in range(len(breaker)):
                if breaker[correct] == guess:
                    scoreboard[correct] = breaker[correct]
            play_game()
        elif guess not in breaker:
            print("dumbass")
            past_guesses.append(guess)
            WRONG.append("X")
            print(" X" * len(WRONG),"\n",f'{8 - len(WRONG)} {"guess" if 8 - len(WRONG) == 1 else "guesses"} left!')
            play_game()





if __name__ == "__main__":
    play_game()
