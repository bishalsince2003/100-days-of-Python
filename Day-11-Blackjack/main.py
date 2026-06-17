import random
import art 
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_list=[]
user_list=[]
card1=cards[random.randint(0,12)]
card2=cards[random.randint(0,12)]
computer_list.append(card1)
computer_list.append(card2)
print(f"Computer's card is [X,{card2}]")

card3=cards[random.randint(0,12)]
card4=cards[random.randint(0,12)]
user_list.append(card3)
user_list.append(card4)

print(f"Your's card is [{card3},{card4}]")

decision_of_computer=["n","y","n"]

want_more=True
while want_more==True:
    decision=input("Would you like to add one more card ? Type 'Y' for yes , otherwise 'N' for no. ").lower()
    if decision=="y":
        card5 = cards[random.randint(0, 12)]
        user_list.append(card5)
        print(user_list)
        sum=0
        for score in user_list:
            sum+=score
        if sum>21:
            print("You lose.")
            exit()
        elif sum==21:
            print("You win. ")
            exit()
    elif decision=="n":
        want_more=False
        sum=0
        for score in user_list:
            sum+=score
        comp=decision_of_computer[random.randint(0,2)]
        while comp!="n":
            card6 = cards[random.randint(0, 12)]
            computer_list.append(card6)
            card_sum=0

            for card in computer_list:
                card_sum+=card
            if card_sum > 21:
                print("You win.")
                exit()
            elif card_sum == 21:
                print("You lose. ")
                exit()

            comp = decision_of_computer[random.randint(0, 1)]
            print(computer_list)
        print(f"User cards: {user_list}")
        print(f"Computer cards: {computer_list}")

        sum2 = 0
        for score in computer_list:
            sum2 += score

        if sum < 22 and sum > sum2:
            print("You win")
            exit()
        elif sum2<22 and sum2>sum:
            print("Computer won")
            exit()
        elif sum==sum2:
            print("Match drawn.")
            exit()