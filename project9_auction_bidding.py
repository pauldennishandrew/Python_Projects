# TODO-1: Ask the user for inpu
import art
print(art.logo)
print("Welcome to the secret auction program.")
auction ={}
should_continue = True
while should_continue:
   name = input("What is your name?:")
   bid = int(input("What's your bid?:$"))
   auction[name]=bid
   question=input("Are there any other bidders? Type 'yes' or 'no'.\n")
   output =""
   for i in question:
       char = i
       if char == char.lower():
        output += char
       else:
        char = char.lower()
        output += char
   if output == "yes":
       print("\n"*50)
   else:
       should_continue = False
value = 0
for item in auction:
    if auction[item] > value:
        value = auction[item]
    else:
        value = value
key_list=list(auction.keys())
val_list =list(auction.values())
index_val =val_list.index(value)
print(f"The winner is {key_list[index_val]} with a bid of ${value}")




