from art import logo
from art import vs
import random
import game_data
A = random.choice(game_data.data)
B = random.choice(game_data.data)
count=0

def user_a(A,B):
    global count
    if A['follower_count'] > B['follower_count']:
        count += 1
        return f"You are right.count = {count}"
    else:
        return f"Sorry that's wrong. Final score = {count}"

def user_b(B,A):
    global count
    if B['follower_count'] > A['follower_count']:
        count += 1
        return f"You are right.count = {count}"
    else:
        return f"Sorry that's wrong. Final score = {count}"
def again():
    print(logo)
    print( f"You are right.count = {count}")
    A = random.choice(game_data.data)
    print(f"Compare A :{A['name']},{A['description']}, from {A['country']}")
    print(vs)
    B = random.choice(game_data.data)
    print(f"Against B :{B['name']},{B['description']}, from {B['country']}")
    user_choice = input("Who has more followers? type 'A' or Type 'B'")
    if user_choice == 'A':
        user_input = A
        other_input = B
        result = user_a(user_input, other_input)

    else:
        user_input = B
        other_input = A
        user_b(user_input, other_input)
        result = user_b(user_input, other_input)

    if result == f"Sorry that's wrong. Final score = {count}":

        print("\n" * 15)
        print(logo)
        print(result)
    else:
        print("\n" * 15)
        again()


def select():
    Guess_higher_lower = True
    while Guess_higher_lower:
        print(logo)
        A = random.choice(game_data.data)
        print(f"Compare A :{A['name']},{A['description']}, from {A['country']}")
        print(vs)
        B = random.choice(game_data.data)
        print(f"Against B :{B['name']},{B['description']}, from {B['country']}")
        user_choice=input("Who has more followers? type 'A' or Type 'B'")
        if user_choice =='A':
            user_input =A
            other_input=B
            result= user_a(user_input,other_input)

        else:
            user_input = B
            other_input =A
            user_b(user_input,other_input)
            result = user_b(user_input, other_input)


        if result ==  f"Sorry that's wrong. Final score = {count}":
            Guess_higher_lower =False
            print("\n"*15)
            print(logo)
            print(result)
        else:
            Guess_higher_lower = False
            print("\n"*15)
            again()
select()






