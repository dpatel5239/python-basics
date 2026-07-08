                     # **Arithmetic , Assignment, Comparison & Logical Operators in Python**
num1 = 10
num2 = 5

# arithmetic operators are used to perform mathematical operations on numbers
# Addition
print(num1 + num2)
# Subtraction
print(num1 - num2)
# Multiplication 
print(num1 * num2)
# Division gives the quotient of the division of num1 by num2 as a float
print(num1 / num2)
#floor division gives the quotient of the division of num1 by num2 rounded down to the nearest integer
print(num1 // num2)
# Modulo operator gives the remainder of the division of num1 by num2     
print(num1 % num2)
# Exponentiation num1 raised to the power of num2
print(num1 ** num2)

# Assignment operators are used to assign values to variables
x = 10  # assigns the value 10 to the variable x
x += 5  # adds 5 to the current value of x and assigns the result back to x (x = x + 5)
print(x)    
x -= 3  # subtracts 3 from the current value of x and assigns the result back to x (x = x - 3)
print(x)
x *= 2  # multiplies the current value of x by 2 and assigns the result back to x (x = x * 2)
print(x)
x /= 4  # divides the current value of x by 4 and assigns the result back to x (x = x / 4)
print(x)        
x//= 2  # performs floor division on the current value of x by 2 and assigns the result back to x (x = x // 2)
print(x)    
x%= 3  # performs modulo operation on the current value of x by 3 and assigns the result back to x (x = x % 3)
print(x)    
x**= 4  # raises the current value of x to the power of 4 and assigns the result back to x (x = x ** 4)
print(x)

# Comparison operators are used to compare two values and return a boolean result (True or False)
a = 10
b = 5

print(a == b)  # checks if a is equal to b
print(a != b)  # checks if a is not equal to b
print(a > b)   # checks if a is greater than b
print(a < b)   # checks if a is less than b
print(a >= b)  # checks if a is greater than or equal to b
print(a <= b)  # checks if a is less than or equal to b

# Logical operators are used to combine multiple boolean expressions and return a boolean result
p= True
q = False   

print(p and q)  # returns True if both p and q are True, otherwise returns False
print(p or q)   # returns True if at least one of p or q is True, otherwise returns False
print(not p)    # returns the opposite of p, if p is True it returns False, and if p is False it returns True
