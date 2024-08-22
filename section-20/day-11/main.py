import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = []
dealer_cards = []
another_game = ""

def card(your_score, your_cards, dealer_cards):
    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {dealer_cards}")

def game():
    print("\n" * 100)
    print(logo)
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    your_score = your_cards[0] + your_cards[1]
    dealer_cards.append(random.choice(cards))
    card(your_score, your_cards, dealer_cards)
    dealer_more = True
    another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while another == "y":
        your_score = 0
        your_cards.append(random.choice(cards))
        for i in your_cards:
            your_score += i
        card(your_score, your_cards, dealer_cards)
        if your_score <= 21:
            another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        else:
            another = "n"
            print(f"Your final hand: {your_cards}, final score: {your_score}: ")
            print("You went over. You lose")
    while dealer_more == True:
        dealer_score = 0
        dealer_cards.append(random.choice(cards))
        for i in dealer_cards:
            dealer_score += i
        if dealer_score >= 17: 
            dealer_more = False
            print(f"Your final hand: {your_cards}, final score: {your_score}")
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
            if dealer_score <= 21:
                if dealer_score > your_score:
                    print("You lose")
                elif your_score > dealer_score:
                    print("You win")
                else:
                    print("DRAW")
            else:
                print("Opponent went over. You win")
    

if input("Do you want to play a game of blackjack? Type (y) or (n): ").lower() == "y":
    game()
    another_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    while another_game == "y":
        your_cards = []
        dealer_cards = []
        game()
        another_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    