#Silent Auction Program
print("****Welcome to silent auction program*****")
import os
def find_winner(bidder_details):
    highest_bidding =0
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price>highest_bidding:
            highest_bidding = bidding_price
            winner = bidder
    print(f"The highest bidding is of {winner}  with bidding price {highest_bidding}")

bidder_details ={}
end_of_bidding = False
while not end_of_bidding:
    name = input("Enter the name:")
    bid = int(input("Enter your bid:"))
    bidder_details[name]=bid
    more_bidder = input("Are there any other bidder? Type 'yes or 'no").lower()
    if more_bidder =='no':
        end_of_bidding = True
        find_winner(bidder_details)
    elif more_bidder == "yes":
        os.system("cls")








