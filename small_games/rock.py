import random

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer_choice = random.randint(0, 2)
print(f"Computer chose: ")

if your_choice == 0:
    if computer_choice == 0:
        print("The game is tie")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("You win")
elif your_choice == 1:
    if computer_choice == 1:
        print("The game is tie")
    elif computer_choice == 0:
        print("You win")
    else:
        print("You lose")
elif your_choice == 2:
    if computer_choice == 2:
        print("The game is tie")
    elif computer_choice == 0:
        print("You win")
    else:
        print("You lose")
else:
    print("You didn't put a correct number.")