import art
import random
print(art.logo1)

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")
number=random.randint(1,100)

difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level=="easy":
    lives_count=10
elif difficulty_level=="hard":
    lives_count=5
game_over=False

while game_over==False:
    print(f"You have {lives_count} attempts remaining to guess the number. ")
    user_number=int(input("Make a guess: "))
    if user_number==number:
        print(f"You got it. The answer was {number}. ")
        game_over=True
    elif user_number> number:
        lives_count-=1
        if lives_count>0:
            print("Too high. \nGuess again. ")
        else:
            print("You've run out of guesses. Refresh the page to run again.")
            print(f"The actual answer was {number}. ")
            game_over=True
    else:
        lives_count-=1
        if lives_count>0:
            print("Too low. \nGuess again.")
        else:
            print("You've run out of guesses. Refresh the page to run again.")
            print(f"The actual answer was {number}. ")
            game_over = True
