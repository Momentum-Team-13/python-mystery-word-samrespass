import random
import sys
from tkinter.messagebox import QUESTION
import inquirer

words = open("words.txt", "r")
words_two = words.read()
word_bank = words_two.split()
hell = []
str = ' '
WRONG = []
past_guesses = []
difficulty = [
    inquirer.List('mode',
    message = "Choose Your Difficulty",
    choices = ['Hell','Hard','Medium','Soft']
    )
]

play_again = [
    inquirer.List('play',
    message= "Wanna Go Again?",
    choices = ['Yeah!','Nah...']
    )
]

def choose_difficulty():
    answers = inquirer.prompt(difficulty)
    if 'Hard' in answers.values():
        guess_me = random.choice(word_bank)
        while len(guess_me) < 8:
            guess_me = random.choice(word_bank)
        print("Hard Mode Selected")
        return board_maker(guess_me)
    if 'Medium' in answers.values():
            guess_me = random.choice(word_bank)
            while len(guess_me) < 6 or len(guess_me) > 8:
                guess_me = random.choice(word_bank)
            print("Medium Mode Selected")
            return board_maker(guess_me)
    if 'Soft' in answers.values():
            guess_me = random.choice(word_bank)
            while len(guess_me) > 6:
                guess_me = random.choice(word_bank)
            print("Soft Mode Selected")
            return board_maker(guess_me)
    if 'Hell' in answers.values():
            guess_me = random.choice(word_bank)
            breaker = list(guess_me)
            new_board = "_" * len(breaker)
            scoreboard = list(new_board)
            hell.append("hell")
            print("Heaven or Hell Let's Rock")
            return play_game(scoreboard, breaker)

def board_maker(guess_me):
    breaker = list(guess_me)
    new_board = "_" * len(breaker)
    scoreboard = list(new_board)
    return play_game(scoreboard, breaker)


def play_game(scoreboard, breaker):
    if len(WRONG) == 8:
        print(f"\nLOSER!\nThe Word Was: {''.join(breaker)}\n")
        mulligan = inquirer.prompt(play_again)
        if 'Nah...' in mulligan.values():
            sys.exit(0)
        else:
            WRONG.clear()
            hell.clear()
            past_guesses.clear()
            choose_difficulty()
    if scoreboard == breaker:
        print(f"'\n',{''.join(breaker)}\nYOU WIN!")
        mulligan = inquirer.prompt(play_again)
        if 'Nah...' in mulligan.values():
            sys.exit(0)
        else:
            WRONG.clear()
            hell.clear()
            past_guesses.clear()
            choose_difficulty()

    else:
        print(f"{str.join(scoreboard)} \n GUESS ME!")
        guess = input("Pick A Letter: ").lower()
        if not guess.isalpha():
            print("Letters only!")
            play_game(scoreboard, breaker)
        elif len(guess) > 1:
            print("One at a time buddy.")
            play_game(scoreboard, breaker)
        elif guess in past_guesses:
            print("You Already Tried That...")
            play_game(scoreboard, breaker)
        elif guess in breaker:
            print("good guess!")
            past_guesses.append(guess)
            for correct in range(len(breaker)):
                if breaker[correct] == guess:
                    scoreboard[correct] = breaker[correct]
            play_game(scoreboard, breaker)
        elif guess not in breaker:
            past_guesses.append(guess)
            WRONG.append("X")
            print("\nwrong, dumbass\n","X" * len(WRONG),"\n",f'{8 - len(WRONG)} {"guess" if 8 - len(WRONG) == 1 else "guesses"} left!')
            if "hell" in hell and len(WRONG) != 8:
                past_guesses.clear()
                hell_game()
            play_game(scoreboard, breaker)

def hell_game():
    guess_me = random.choice(word_bank)
    breaker = list(guess_me)
    new_board = "_" * len(breaker)
    scoreboard = list(new_board)
    print("\nThe Hell Continues")
    return play_game(scoreboard, breaker)





if __name__ == "__main__":
    choose_difficulty()
