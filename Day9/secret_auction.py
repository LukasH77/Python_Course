# from replit import clear
from secret_auction_art import logo

print(logo)
print("Welcome to the secret auction!")
bids = {}
bidding = True
while bidding:
    name = input("Please enter your name.\n")
    bid = int(input(f"How much are you bidding, {name}?\n$"))
    bids[name] = bid
    # anything but "yes" terminates the program
    bidding = input("Are there more bidders? Type yes or no.\n") == "yes"
    # the clear function does not seem to work in this environment
    # clear()
    # workaround with linebreaks
    print("\n" * 100)

max = 0
buyer = ""
for bidder in bids:
    bid = bids[bidder]
    if bid > max:
        max = bid
        buyer = bidder
print(f"The item has been sold for ${max} to {buyer}")
