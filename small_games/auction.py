

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for person in bidding_record:
        bid_amount = bidding_record[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of {highest_bid}.")


while not bidding_finished:
    name = input("What's your name?\n")
    price = int(input("What's your bid? $"))
    bids[name] = price
    bidders = input("Are there other bidders? Type 'yes' or 'no': ")
    if bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif bidders == "yes":
        continue










