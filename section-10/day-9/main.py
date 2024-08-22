from art import logo

print(logo)

print("Welcome to the secret auction program.")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest = 0
    for i in bidding_dictionary:
        if auction[i] > highest:
            highest = auction[i]
            winner = i

    print(f"The winner is {winner} with a bid of ${highest}")

auction = {}
more = "yes"

while more == "yes":
    name = input("What is your name?: ")
    auction[name] = float(input("What's your bid?: $"))
    more = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    print("\n" * 100)

find_highest_bidder(auction)


