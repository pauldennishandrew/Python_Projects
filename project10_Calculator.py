import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return  n1 * n2
def divide(n1,n2):
    return n1 / n2
infinite_loop = True
Continue_calculating = True
while infinite_loop:
    n1 = float(input("What the first number?:"))

    while Continue_calculating:
        calculation ={
            "+":add ,
            "-":subtract,
            "*":multiply,
            "/":divide
        }
        for item in calculation:
            print(item)
        select = input("pick an operation:")
        n2 =float(input("What's the next number?:"))
        if select == "+":
           result = add(n1,n2)
        elif select == "-":
           result = subtract(n1,n2)
        elif select == "*":
            result = multiply(n1,n2)
        else:
            result = divide(n1,n2)
        print(f"{n1} {select} {n2}= {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            n1 = result
        else:
            Continue_calculating = False
            print("\n"*25)



