import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for rock, Type 1 for paper and Type 2 for Scissors. \n"))
if user_input>2 or user_input<0:
    print("Wrong input")
    exit()
print("Your choice:\n")
print(game[user_input]+"\n")
print("Computer:\n")
game_input=random.randint(0,2)
print(game[game_input]+"\n")
print("Result:\n")

if user_input==game_input:
    print("Game tie, pls retry.")
elif user_input==0 and game_input==1:
    print("You lose")
elif user_input==0 and game_input==2:
    print("You Win")
elif user_input==1 and game_input==0:
    print("You win")
elif user_input==1 and game_input==2:
    print("You lose")
elif user_input==2 and game_input==0:
    print("You lose")
elif user_input==2 and game_input==1:
    print("You Win")
