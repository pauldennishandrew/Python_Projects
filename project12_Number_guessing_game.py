import random
from art import logo
EASY_LIMIT =10
HARD_LIMIT =5
def compare_guessing_num(c_num,u_num):
    if u_num not in range(1,101):
        return "Give a value between 1 and 100"
    if u_num == c_num:
        return "You win! you guessed the correct number."
    elif u_num > c_num:
        return "Too High\nGuess again"
    elif u_num < c_num:
        return "Too Low\nGuess again"


def easy():
    EASY_LIMIT=10
    easy_level = True
    while easy_level and  EASY_LIMIT >=1:
           print(f"you have {EASY_LIMIT} attempts to guess the number! ")
           user_number = int(input("Make a guess:"))
           output = compare_guessing_num(computer_number, user_number)
           if output== "You win! you guessed the correct number.":
             print(output)
             easy_level=False
           else:
               print(output)
               EASY_LIMIT -= 1
    return "Sorry Your attempts are over!"
def hard():
    HARD_LIMIT=5
    hard_level = True
    while  hard_level and HARD_LIMIT>=1:
           print(f"you have {HARD_LIMIT} attempts to guess the number! ")
           user_number = int(input("Make a guess:"))
           output = compare_guessing_num(computer_number, user_number)
           if output== "You win! you guessed the correct number.":
             print(output)
             hard_level=False
           else:
               print(output)
               HARD_LIMIT -= 1
    return "Sorry Your attempts are over!"


print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
computer_number=random.randint(1,100)
user_select=input(f"Choose your difficulty: Type 'easy' or 'hard':").lower()
if user_select == "easy":
    result=easy()
    print(result)
else:
    result=hard()
    print(result)




