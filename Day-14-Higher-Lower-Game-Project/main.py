import art
import game_data
import random

def generate_new_num():
    num = random.randint(1, len(game_data.data) - 1)
    return num

score=0


print(art.logo)

# num = random.randint(1,len(game_data.data)-1)
# num1 = random.randint(1,len(game_data.data)-1)


game_over=False
person = game_data.data[generate_new_num()]
while game_over == False:
    person1 = game_data.data[generate_new_num()]
    print(f"Compare A: {person['name']}, {person['description']}, {person['country']}, ")

    print(art.vs)

    print(f"Against B: {person1['name']}, {person1['description']}, {person1['country']}, ")

    user_input= input("Who has more followers? Type 'A' or 'B': ")
    computer_value=0
    user_value=0
    if user_input=="B":
        user_value=person1['follower_count']
        computer_value=person['follower_count']
    elif user_input=="A":
        user_value = person['follower_count']
        computer_value = person1['follower_count']
    else:
        print("invalid input!")

    if user_value > computer_value:
       score+=1
       print(f"You're right! Current score: {score}")
       person=person1
    elif computer_value > user_value:
        print(f"Sorry that's wrong. Final score: {score}")
        game_over=True
