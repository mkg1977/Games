import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========          
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /    |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= 
''']


world_list = ["bitti", "proshmita", "diana", "manik", "tennessee",
"alabama", "atlanta", "georgia", "ireland", "australia", "bangladesh",
"india", "bittu", "hritom", "netflix", "watch", "elsa", "indianna",
"split", "science", "planet", "galaxy", "baby-boss", "space-jam",
"pokai", "noodles", "icecream", "cake", "birthday", "banana", "orange",
"apple", "strawberry"]

#from hangman_words import word_list
chosen_word = random.choice(world_list)

lives = 6
from hangman_art import logo, stages
print(logo)
#print(f'The chossen word is: {chosen_word}')

display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)



game_end = False

while game_end != True:
    guess = input("Guess a letter to save the hangman: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_end = True
            print("************* ************* *************")
            print("* You loose * * You loose * * You loose *")
            print("************* ************* *************")
            print(f"The actual word is: {chosen_word}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print("=========== =========== ===========")
        print("| You win | | You win | | You win |")
        print("=========== =========== ===========")

 
    print(stages[lives])