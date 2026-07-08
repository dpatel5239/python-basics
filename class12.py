#                                              ** conditional  statements **

# 1) if block 
age = int(input("Enter your age : "))
if age >=18 :
    print("congrates you can cast your vote !")
print("Rest of the programme !!")

# 2) if - else block 
gender = str(input("enter your gender (M) for male and (F) for female !!"))
if gender == "M" or gender == "F":
    print("you are valid person")
else:
    print("you  are not a valid person ")

# 3) if-elif-else 
marks = float(input("Enter your marks : "))
if marks>=90 :
    print("your grade is \"A\"")
elif marks>=80 and marks<90:
    print("your grade is \"B\"")
elif marks<=70 and marks<80:
    print("your grade is \"C\"")
elif marks<=60 and marks<70:
    print("your grade is \"D\"")                                                          
else :
    print("your grade is \"F\"")

# 4) nested if block 
if marks >= 60: 
    print("congratulation you are passed the exam !! ")
    if marks <=90:
        print("your grade is \"A\"")
    elif marks>=80 and marks<90:
        print("your grade is \"B\"")
    elif marks<=70 and marks<80:
        print("your grade is \"C\"")
    elif marks<=60 and marks<70:
        print("your grade is \"D\"") 
else :
    print("you have failed ; try next time !! ")

# 5) ternary operater 
#syntax => statement 1 if condition else statement 2 
number = int(input("enter any interger"))
print("EVEN") if number % 2 == 0 else print("ODD")