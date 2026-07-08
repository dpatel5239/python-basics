############################################### roll a dice ##################################################
import random
print("Welcome to the game of rolling a dice. ")

while True:
    choice = input("press 'enter' to roll the dice or 'q' to quit ")
    choice = choice.strip()
    if choice == 'q':
        print("Thanks for playing the game , bye !!!")
        break
    elif choice == "":
        number = random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print("Invalid input !!")
