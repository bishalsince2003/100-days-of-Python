import random
from art import logo
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(cards)
    return card

def calculate_score(list):
    """Take a list of cards and return the calculated score from the cards. """
    if sum(list)==21 and len(list)==2:
        return 0
    if 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)
    return sum(list)

    # sum=0
    # for key in list:
    #     sum+=key
    # if sum==21:
    #     for key in user_cards:
    #         if key==11:
    #             return 0
    # elif sum>21:
    #     for key in user_cards:
    #         if key==11:
    #             user_cards.remove(11)
    #             user_cards.append(1)
    # else:
    #     return sum
def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0 :
        return "Lose , opponent has a blackjack"
    elif u_score == 0 :
        return "Win with a blackjack"
    elif u_score>21:
        return "You went over. You lose! "
    elif c_score>21:
        return "Opponent went over. You win!"
    elif u_score>c_score:
        return "You Win"
    else:
        return "You Lose"
def play_game():
    print(logo)
    user_cards=[]
    # user_cards.append(deal_card())
    # user_cards.append(deal_card())
    # print(user_cards)

    computer_cards=[]
    # computer_cards.append(deal_card())
    # computer_cards.append(deal_card())
    # print(computer_cards)
    computer_score = -1
    user_score = -1

    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            new_card=input("Would you like to draw another card: Type 'Y' for yes, Otherwise 'N' for no.").lower()
            if new_card=="y":
                user_cards.append(deal_card())
            elif new_card=="n":
                is_game_over=True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score= calculate_score(computer_cards)

    print(f"Computer cards: {computer_cards} and computer score: {computer_score}")
    print(f"Your cards: {user_cards} and your score: {user_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack, type 'y' or 'n': ") == "y":
    print("\n"*20)
    play_game()