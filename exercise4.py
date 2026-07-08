####################################### number guesing problem    ###################################################
num = 43
print("wellcome to a number guessing game we have a number that needs to be guessed. you have 10 chances \n")

print("The secret number is between 1 to 50 \n")
print("You have 10 chances left \n")
attempts = 10

while True:
    your_num = int(input("Enter your guess :"))


    if your_num <num :
        print("Your guess is wrong!! try higher\n")
    
    elif your_num>num :
        print("Your guess is wrong!! try lower \n")
       
    elif your_num==num :
        print("Congrats your guess is correct !\n")
        print(f"The number was {num}. Game over\n")
        break

    else:
        print("Your given number is invalid")
    
    print(f"You have {attempts} chances left \n")
    attempts -= 1
    if attempts == 0:
        print(f"game over !! You used all chances . The number was {num}\n")
        break


    
   
  

