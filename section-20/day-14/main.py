from art import logo, vs
from game_data import data
import random


def lists(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

score = 0
game = True

b = random.choice(data)
print(logo)
while game:
    a = b
    b = random.choice(data)

    if a == b:
        b = random.choice(data)
    
    print(f"Compare A: {lists(a)}.")
    print(vs)
    print(f"Against B: {lists(b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a["follower_count"] > b["follower_count"]:
        answer = "a"
    else:
        answer = "b"
    
    if answer == guess:
        for i in range(25):
            print("")
        print(logo)
        score += 1
        print(f"You're right! Current score {score}")
    else:
        for i in range(25):
            print("")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False