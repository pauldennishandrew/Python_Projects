# # # # # # # # # # # print("how are you","Andrew paul")
# # # # # # # # # # for i in range(5):
# # # # # # # # # #     print(i,end="")
# # # # # # # # # #
# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     list = []
# # # # # # # # #     for _ in range(int(input())):
# # # # # # # # #         name = input()
# # # # # # # # #         score = float(input())
# # # # # # # # #         list.append([name, score])
# # # # # # # # #     # print(list)
# # # # # # # # #     list.sort(key=lambda x: x[1])
# # # # # # # # #     a = len(list)
# # # # # # # # #     # print(list)
# # # # # # # # #
# # # # # # # # #     for _  in range(a):
# # # # # # # # #         if list[0][1] == list[1][1]:
# # # # # # # # #             list.remove(list[0])
# # # # # # # # #     list2 = list
# # # # # # # # #     new_list =[]
# # # # # # # # #     for i in range(len(list2)):
# # # # # # # # #         if list2[i][1]==list[1][1]:
# # # # # # # # #             new_list.append(list[i][0])
# # # # # # # # #     new_list.sort()
# # # # # # # # #     for item in new_list:
# # # # # # # # #         print(item)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # if __name__ == '__main__':
# # # # # # # #     n = int(input())
# # # # # # # #     student_marks = {}
# # # # # # # #     for _ in range(n):
# # # # # # # #         name, *line = input().split()
# # # # # # # #         scores = list(map(float, line))
# # # # # # # #         student_marks[name] = scores
# # # # # # # #     query_name = input()
# # # # # # # # output = list(student_marks[query_name])
# # # # # # # # per = sum(output)/len(output)
# # # # # # # # print("%.2f" % per)
# # # # # # #
# # # # # # # def split_and_join(line):
# # # # # # #     # write your code here
# # # # # # #     output = line.split(" ")
# # # # # # #     # print(output)
# # # # # # #     a = len(output)
# # # # # # #     # print(a)
# # # # # # #     str = ""
# # # # # # #     for item in range(a):
# # # # # # #         if item < a-1 and item != a:
# # # # # # #           str =str+ output[item] + "-"
# # # # # # #
# # # # # # #     return str
# # # # # # #
# # # # # # #
# # # # # # # if __name__ == '__main__':
# # # # # # #     line = input()
# # # # # # #     result = split_and_join(line)
# # # # # # #     print(result)
# # # # # # def mutate_string(string, position, character):
# # # # # #     l = list(string)
# # # # # #     l.insert(position, character)
# # # # # #     del l[position+1]
# # # # # #     l1=""
# # # # # #     for item in l:
# # # # # #         l1 +=item
# # # # # #     return  l1
# # # # # #
# # # # # #
# # # # # #
# # # # # # if __name__ == '__main__':
# # # # # #     s = input()
# # # # # #     i, c = input().split()
# # # # # #     s_new = mutate_string(s, int(i), c)
# # # # # #     print(s_new)
# # # # # # cook your dish here
# # # # # test_case = int(input())
# # # # # for i in range(test_case):
# # # # #     num_of_inp = int(input())
# # # # #     x = map(int, input().split())
# # # # #     l = list(x)
# # # # #     sunil_position = l[-1]
# # # # #     position = True
# # # # #     i=-2
# # # # #     while position:
# # # # #         if l[i] < sunil_position and l[i] <= sunil_position / 2:
# # # # #             i -=1
# # # # #             l.remove(l[i])
# # # # #         else:
# # # # #             position = False
# # # # #     print(len(l))
# # # # #
# # # # l=5
# # # # print(l/2)
# # # test_case = int(input())
# # # for _ in range(test_case):
# # #     num_of_inp = int(input())
# # #     l = list(map(int, input().split()))
# # #     sunil_position = l[-1]
# # #
# # #     i = len(l) - 2  # Start from the second last element
# # #     while i >= 0:
# # #         if l[i] < sunil_position:
# # #             if l[i] <= sunil_position / 2:
# # #                 l.pop(i)  # Remove element if it satisfies the condition
# # #                 i -= 1
# # #             else:
# # #                 i = -1
# # #                 # Move to the previous element
# # #
# # #     print(len(l))
# # # cook your dish here
# # # test_cases = int(input())
# # # for _ in range(test_cases):
# # #     n, k = map(int, input().split())
# # #     arr = list(map(int, input().split()))
# # #     arr=sorted(arr)
# # #     print(arr)
# # # Python program to find GCD of two numbers
# #
# #
# # # Function to find gcd of two numbers
# # # def gcd(a, b):
# # #
# # #     # Find minimum of a and b
# # #     result = min(a, b)
# # #
# # #     while result:
# # #         if a % result == 0 and b % result == 0:
# # #             break
# # #         result -= 1
# # #
# # #     # Return the gcd of a and b
# # #     return result
# # #
# # #
# # # # Driver Code
# # # if __name__ == '__main__':
# # #     a = 0
# # #     b = 56
# # #     print(f"GCD of {a} and {b} is {gcd(a, b)}")
# # import random
# # import sqlite3
# # from tabulate import tabulate
# #
# # from project12_Number_guessing_game import EASY_LIMIT
# #
# # # Word sets for the game
# # WORD_SETS = {
# #     'Animals': ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra'],
# #     'Shapes': ['square', 'triangle', 'rectangle', 'circle', 'ellipse', 'rhombus', 'trapezoid'],
# #     'Places': ['Cairo', 'London', 'Paris', 'Baghdad', 'Istanbul', 'Riyadh']
# # }
# #
# # # Hangman graphics for display
# # HANGMAN_GRAPHICS = [
# #     """
# #        --------
# #        |      |
# #        |      O
# #        |     \\|/
# #        |      |
# #        |     / \\
# #        -
# #     """,
# #     """
# #        --------
# #        |      |
# #        |      O
# #        |     \\|/
# #        |      |
# #        |     /
# #        -
# #     """,
# #     """
# #        --------
# #        |      |
# #        |      O
# #        |     \\|/
# #        |      |
# #        |
# #        -
# #     """,
# #     """
# #        --------
# #        |      |
# #        |      O
# #        |     \\|
# #        |      |
# #        |
# #        -
# #     """,
# #     """
# #        --------
# #        |      |
# #        |      O
# #        |      |
# #        |      |
# #        |
# #        -
# #     """,
# #     """
# #        --------
# #        |      |
# #        |      O
# #        |
# #        |
# #        |
# #        -
# #     """,
# #     """
# #        --------
# #        |      |
# #        |
# #        |
# #        |
# #        |
# #        -
# #     """
# # ]
# #
# #
# # # SQLite setup for Hall of Fame
# # def setup_database():
# #     conn = sqlite3.connect('hangman_records.db')
# #     c = conn.cursor()
# #     c.execute('''CREATE TABLE IF NOT EXISTS hall_of_fame
# #                  (name TEXT, level TEXT, remaining_lives INTEGER)''')
# #     conn.commit()
# #     return conn
# #
# #
# # def update_hall_of_fame(name, level, lives):
# #     conn = setup_database()
# #     c = conn.cursor()
# #     # Check if a better record exists
# #     c.execute("SELECT * FROM hall_of_fame WHERE level = ? ORDER BY remaining_lives DESC LIMIT 1", (level,))
# #     result = c.fetchone()
# #
# #     if result is None or lives > result[2]:
# #         # Update record if new record is better
# #         c.execute("DELETE FROM hall_of_fame WHERE level = ?", (level,))
# #         c.execute("INSERT INTO hall_of_fame (name, level, remaining_lives) VALUES (?, ?, ?)", (name, level, lives))
# #         conn.commit()
# #
# #     conn.close()
# #
# #
# # def display_hall_of_fame():
# #     conn = setup_database()
# #     c = conn.cursor()
# #     c.execute("SELECT * FROM hall_of_fame")
# #     records = c.fetchall()
# #     conn.close()
# #
# #     print("\nHALL OF FAME")
# #     if records:
# #         print(tabulate(records, headers=['Player Name', 'Level', 'Remaining Lives'], tablefmt='grid'))
# #     else:
# #         print("No records found.")
# #
# #
# # # Function to select difficulty
# # def select_difficulty():
# #     while True:
# #         print("\nSelect Difficulty Level:")
# #         print("1. Easy")
# #         print("2. Moderate")
# #         print("3. Hard")
# #         choice = input("Enter choice: ")
# #         if choice in ['1', '2', '3']:
# #             return int(choice)
# #         print("Invalid choice. Please select again.")
# #
# #
# # # Function to select word set
# # def select_word_set():
# #     while True:
# #         print("\nSelect word set:")
# #         print("1. Animals")
# #         print("2. Shapes")
# #         print("3. Places")
# #         choice = input("Enter choice: ")
# #         if choice in ['1', '2', '3']:
# #             return ['Animals', 'Shapes', 'Places'][int(choice) - 1]
# #         print("Invalid choice. Please select again.")
# #
# #
# # # Function to pick a word
# # def pick_word(difficulty):
# #     if difficulty == 1 or difficulty == 2:  # Easy or Moderate
# #         word_set = select_word_set()
# #     else:  # Hard
# #         word_set = random.choice(list(WORD_SETS.keys()))
# #
# #     return random.choice(WORD_SETS[word_set])
# #
# #
# # # Function to display hangman
# # def display_hangman(lives, difficulty):
# #     if difficulty == 2 or difficulty == 3:
# #         # Skip two stages for Moderate and Hard (6 lives instead of 8)
# #         print(HANGMAN_GRAPHICS[6 - lives])
# #     else:
# #         print(HANGMAN_GRAPHICS[8 - lives])
# #
# #
# # # Function to play the game
# # def play_game(player_name, difficulty):
# #     lives = 8 if difficulty == 1 else 6
# #     secret_word = pick_word(difficulty)
# #     guessed_word = ['_'] * len(secret_word)
# #     guessed_letters = set()
# #     print("\nLet's start the game!")
# #
# #     while lives > 0 and ''.join(guessed_word) != secret_word:
# #         display_hangman(lives, difficulty)
# #         print("Word: ", ' '.join(guessed_word))
# #         guess = input("Guess a letter: ").lower()
# #
# #         if not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
# #             print("Invalid input or already guessed letter.")
# #             continue
# #
# #         guessed_letters.add(guess)
# #
# #         if guess in secret_word:
# #             for i, letter in enumerate(secret_word):
# #                 if letter == guess:
# #                     guessed_word[i] = guess
# #         else:
# #             lives -= 1
# #
# #     if ''.join(guessed_word) == secret_word:
# #         print(f"Congratulations {player_name}! You've guessed the word '{secret_word}' with {lives} lives remaining.")
# #         update_hall_of_fame(player_name, ['Easy', 'Moderate', 'Hard'][difficulty - 1], lives)
# #     else:
# #         print(f"Sorry {player_name}, you've lost. The word was '{secret_word}'.")
# #
# # # Main menu for user
# # play_game("andrew", "Easy")
# original_list = [1, 1,1,2,2]
# value_to_remove = 1
#
#
# original_list.remove(value_to_remove)
# original_list.append(value_to_remove)
# original_list.reverse()
#
# print(original_list)
def remove_common_characters(str1, str2):
    # Convert strings to sets to find common characters
    set1 = set(str1)
    set2 = set(str2)

    # Find common characters
    common_chars = set1.intersection(set2)

    # Remove common characters from both strings
    result_str1 = ''.join([char for char in str1 if char not in common_chars])
    result_str2 = ''.join([char for char in str2 if char not in common_chars])

    return result_str1, result_str2


# Example usage
str1 = "hello"
str2 = "world"
new_str1, new_str2 = remove_common_characters(str1, str2)
print("String 1 after removing common characters:", new_str1)
print("String 2 after removing common characters:", new_str2)
