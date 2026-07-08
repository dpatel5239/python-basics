# dictinory => A dictinoriay is a data type which have keys and values , each comma is seperated by comma and keys and values are seprated with colon 
# notes => it is mutables and any we use any data type for keys and values
# list,set and dic are not allowed as a key for dict .
groceries = {"milk":30,"Biscuits":20,"rice":90,"bread":30}
print(groceries)
print(type(groceries))

#operations in dictinories 
#1) fetching the element or get() function 
print(groceries.get("milk"))

#2) member (in or not in)
print("dal"in groceries)
print("chicken" not in groceries)

#3) update()
sem1_marks = {"maths":78.5,"english":70.0,"physics":86.5}
sem2_marks = {"chemistry":85.5,"biology":80.5}
sem1_marks.update(sem2_marks)
print(sem1_marks)

#4) pop()
groceries.pop("milk")
print(groceries)

#5) keys() => it is the function used to fetch all the keys of the dict.
print(sem1_marks.keys())

#6) values() => it is used to fetch all the values of the dict.
print(sem1_marks.values())

#7) items() => it is used to fetch all the pairs of keys and values in a multiple tuples 
print(sem1_marks.items())
