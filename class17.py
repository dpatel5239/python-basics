###################################### functions and modules ##################################################
# functions are the block of code use to do some task ,it takes some value and does something for us
def greeting_someone():
    print("hello , good morning !")
    print("it's a beautiful day.")

greeting_someone()

#return value => instead of returning functions output we use return to get the value out of the function.
# >>>>>> if you wanted to store the result and reuse it then we use return instead of print() hence the none is removed .


def even_odd(num):
    if num % 2 == 0:
       return "even"
    else:
        return "odd"
result = even_odd(45)
print(result)

def arithmetic(num1,num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1*num2
    
    return add,sub,mul

val1 = int(input("Enter a first number :"))
val2 = int(input("Enter a second number:"))

res1,res2,res3 = arithmetic(val1,val2)
print(f"Addition of {val1} and {val2} is {res1}")
print(f"Diffrence between {val1} and {val2} is {res2}")
print(f"Product of {val1} and {val2} is {res3} ")

# Types of arguments >>>>>
#>>>> 1) positional arguments => it is the type of argument in which we use give the argument and it is in order of their position .
def add(a,b):
    return a + b

result = add(10,5)
print(f"The sum of the numbers is {result}") 

#>>>> 2) default arguments => In this type of argument the value is given first as a default value and then if needed it can be changed .
# note => The non default arguments should not follow the default arguments . it should come first .

def add_1(a,b=10):
    return a+b
result = add_1(10)
print(f"The sum of the given numbers is : {result} ")

#>>>>> 3) keyword argument or name argument => This argument is used to give the different positions and wanted to skip one we use their keywords to access them.

def add_2(a,b=10,c=20):
    print(f"a:{a},b:{b},c:{c}")
    return a+b+c
result = add_2(10)
print(result)

####### variable length positional arguments ############3

# => it is used to get the multipule arguments as per the user and it can be any variable but starts with (*).
def add_3 (*args):
    return sum(args)
result = add_3(1,2,3,4,5,6,7,8,9,10)
print(result)

def student_detail(sid,sname,*marks):
    
    if len(marks)==0:
        print(f"{sname} with id {sid} was absent ")
    else:
        percentage = sum(marks)/len(marks)
        print(f"{sname} with id {sid} secured {percentage} %")

student_detail(31,"dipak",89,37,45,36,90)
student_detail(32,"mayank",10,3,5,0,1)
student_detail(33,"sugandh",9,3,4,5,3)
student_detail(34,"aftab")
