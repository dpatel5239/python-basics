 # task 1
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")

# task 2
total = 0

for i in range(1, 51):
    total += i

print("The sum of numbers from 1 to 50 is:", total)