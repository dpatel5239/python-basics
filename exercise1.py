                                # Exercise 1: Basic Python Coding
 # area of a triangle when all sides are given
a = float(input(" ENTER THE FIRST SIDE OF THE TRIANGLE: "))
b = float(input(" ENTER THE SECOND SIDE OF THE TRIANGLE: "))
c = float(input(" ENTER THE THIRD SIDE OF THE TRIANGLE: "))

s = (a+b+c)/2 # semi-perimeter of the triangle
area = (s*(s-a)*(s-b)*(s-c))**0.5 # area of the triangle using Heron's formula
print(" THE AREA OF THE TRIANGLE IS: ", round(area, 2))

       # simple interest calculation
p = float(input(" ENTER THE PRINCIPAL AMOUNT: "))
r = float(input(" ENTER THE RATE OF INTEREST: "))       
t = float(input(" ENTER THE TIME IN YEARS: "))
simple_interest = (p*r*t)/100 # simple interest formula
print(" THE SIMPLE INTEREST IS: ", round(simple_interest, 2))

        # compound interest calculation
p = float(input(" ENTER THE PRINCIPAL AMOUNT: "))
r = float(input(" ENTER THE RATE OF INTEREST: ")) 
t = float(input(" ENTER THE TIME IN YEARS: "))

amount = p * (1 + r/100)**t 
compound_interest = amount - p # compound interest formula
print(" THE COMPOUND INTEREST IS: ", round(compound_interest, 2))

