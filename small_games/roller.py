print("Welcome to the rollercoaster!")

height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18 and age >= 12:
        bill = 7
        print("Please pay $7.")
    elif age => 45 and age <= 55:
        print("Everything is going to be ok, have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")


    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 3

    print(f"Your final bill if ${bill}.")
        


else:
    print("Sorry, you have to grow taller before you can ride")