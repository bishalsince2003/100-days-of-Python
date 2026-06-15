# TODO-1: Ask the user for input
import art
print(art.logo)
user_info = {}

bid_end=False
while bid_end !=True:
    name=input("What is your name?\n").upper()
    value=int(input("What's your bid?\n$"))
    user_info[name]=value

    more_bidders=input("Are there more bidders? Type 'Y' for Yes , Otherwise 'N' for No\n").lower()
    if more_bidders=="n":
        n=-1
        winner=""
        for key in user_info:
            if user_info[key]>n:
                n=user_info[key]
                winner=key
        print(f"Winner is {winner} with the bid of ${n}")

        bid_end=True
    else:
        print("\n"*100)

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


