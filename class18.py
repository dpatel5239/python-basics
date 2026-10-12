def check_balance():
    print("checking your balance !!!")
    print(f"your current balance is {balance}")
    print("=====================================")
    

def withdraw():
    global balance
    print("withdrawing your money !!!")
    amount = int(input("ENTER THE AMOUNT TO WITHDRAW "))
    if amount > 0 and amount <= balance :
        balance -= amount
        print(f"rs {amount} has been withdrawed from your account ")
        print(f"The avilable balance is {balance}")
        print("=====================================")
    else :
        print("you have insufficient balance for withdrawl")
        print("=====================================")
    

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"rs {amt} had succesfully deposited to your account")
        print(f"your current balance is rs {balance}")
        print("=====================================")
    else :
        print("you had not enterd the amount yet !!")
        print("=====================================")

def kyc(**doc):

pin = 1122
balance = 10000
kyc_documents={}

while True:
    check_pin = int(input("Enter your four digit pin :"))
    if check_pin == pin :
        print("=====================================")
        print("Hello sir wellcome to Aaj_tak bank")
        print("=====================================")
        break
    else :
        print("Your password is incorrect try again ")
        print("=====================================")
while True:
    print("1 -> Check your balance ")
    print("2 -> withdraw money")
    print("3 -> deposit money")
    print("4 -> quit")
    print("=====================================")
    choose = int(input("choose the operation  which you want to perform among this  "))
    print("=====================================")
    if choose == 1:
        print(f"your bank balance is {check_balance()}")
        print("=====================================")
    elif choose == 2:
        withdraw()
    elif choose == 3:
        amt = int(input("enter your depositting amount : "))
        deposit(amt)
        
    elif choose == 4:
        break
    else :
        print("you have choosen wrong operation !! re-try")
        print("=====================================")

print()
print("THANK FOR YOUR TRANSACTION YOUR DAY WILL BE GOOD !!")