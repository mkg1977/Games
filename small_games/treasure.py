print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': \n").lower()
if choice1 == "left":
    choice2 = input('You have reached at a lake. If you want to swim, type "swim". If you want to ride a boat, type "wait": \n').lower()
    if choice2 == "wait":
        choice3 = input("Cross road again! Which one would you like to choose now? left or right? \n").lower()
        if choice3 == "right":
            choice4 = input("Which door you would like to open? red or blue or yellow? \n").lower()
            if choice4 == "red":
                print("Have a good luck next time. Game over!")
            elif choice4 == "blue":
                print("Bad choice, you found a frog! Game over!")
            elif choice4 == "yellow":
                print("Congratulation! You found a Treasure and you win!")
            else:
                print("This is not a door. Game over")
        else:
            print("A tiger grabbed you. Game over!")
    else:
        print("Crocodile grabbed you. Game over!")
else:
    print("You fell in a hole. Game over!")

