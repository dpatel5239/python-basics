######################################## random module###################################
# module is also known as python files in which python codes are written on it . we have many in build modules which have function likes print() etc .
# few functions of random module
#1) random() => it is used to get random float value between 0.0 to 1.0 where 1 is not included 
import random 
print(random.random())

#2) randint() => it is used to get the random vairaible btw the given  arguments a and b where the both a & b are included 
num = random.randint(1,45)
print(num)

#3) choice(sequence) => it is used to get random items from sequential data type . 
fruits = ["apple","mango","banana","orange"]
print(random.choice(fruits))

#4) shuffle() => it is used to shuffle the sequential data types elements 
random.shuffle(fruits)
print(fruits)


