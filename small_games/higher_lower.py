from art import higher_lower_logo, vs_logo
from high_low_data import data
import random
import os


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}: a {account_description}, from {account_country}.")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


clear = lambda: os.system('cls')
# Display art
score = 0
print(higher_lower_logo)
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
# Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs_logo)
    print(f"Against A: {format_data(account_b)}")

# Format the account data into printable format.


# ask the user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(higher_lower_logo)
## Use if statement to check if user is correct.

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        game_should_continue = False
        print(f"Sorry, That's wrong. Final score: {score}")

#Give user feedback on their guess.

# Score keeping.

# Make the game repeatable.

# Making account at position B become the next account position A.

# Clear the screen between round.