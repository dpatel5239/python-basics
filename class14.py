###################################### while loop ################################################
# it is used when we have to first check the statement and if it true then iterate it till it will get false 
num = 1
while num<5:
    print(num)
    num = num + 1

# infinity while loop 
correct_password = "python"
while True:
    user_password = input ("Enter your password")
    user_password = user_password.strip()
    if user_password == correct_password:
        print("password is correct!")
        break
    else : 
        print("password is incorrect !")
    
