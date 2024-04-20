import random
from art import number_logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_ans(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(number_logo)
    print("Welcome to the Number Guess Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
       print(f"You have {turns} attempts remaining to guess the number.")
       guess = int(input("Make a guess: "))
       
       turns = check_ans(guess, answer, turns)
       if turns == 0:
            print("You have run out of guesses, you lose." )
            return
       elif guess != answer:
           print("Guess again.")

game()


















