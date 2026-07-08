#Tuples => this are also the sequence data types used to store the different data types like list but there is no modification operations on tuple .
# notes => we can also create tuple without using the brakets
t1 = 10,56,"python",2.3
print(len(t1))

         # operations on tuple #
#1. concatenation of tuples => it is used to perform addition btw two tuples 
t2 = (23,"hello",46)
print(t1 + t2)

#2. repitation of the tuples elements => it is used to repeat the tuple elements to the given times 
print(t2*4)

#3. membership  or reverse membership => it is used to check wether the given element is present or not 
print("python" in t1)
print( 10 not in t1)

#4. count() => it is used to find the number of occurance of the given element in the tuple
t3 = (1,0,4,1,5,6,8,5,1)
print(t3.count(1))


#5. index => by using the element the user can check the index value
print(t3.index(5))

