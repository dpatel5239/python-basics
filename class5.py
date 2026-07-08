                      #** print & input  and numeric function in python **
name = " patel dipak ajay "
age = 20
print ( " my name is :", name , "and my age is : ", age )
print ( 10,20,30,40,50, sep = "-" ) # sep is used to specify the separator between the values
print ( "hello", end = " " ) # end is used to specify the end character after the print statement


num1 = input ( " enter the first number : " ) # input function is used to take input from the user, it returns a string
num2 = input ( " enter the second number : " )  
# to perform arithmetic operations on the input numbers, we need to convert them to integers or floats
num1 = int ( num1 ) # converting the input string to an integer
num2 = int ( num2 )
# now we can perform arithmetic operations on num1 and num2 
result = num1 + num2
print ("The sum of num1 and num2 is :", result )

print ( max ( 10, 20, 30 ) ) # max function returns the maximum value among the given arguments
print ( min ( 10, 20, 30 ) ) # min function returns the minimum value among the given arguments
print ( abs ( -10 ) ) # abs function returns the absolute value of the given number 
print ( pow ( 2, 3 ) ) # pow function returns the value of 2 raised to the power of 3
print ( round ( 3.14159, 2 ) ) # round function rounds the given number to the specified number of decimal places, in this case 2 decimal places   

