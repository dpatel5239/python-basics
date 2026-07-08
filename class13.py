                                          # for loop #
#=> it is an iterator based loop which steps through the items of a collection (list ,tuples,sets etc) and executes a block of code repeadly for a number of times .
 #syntax => for variable in sequence:
                    # statement 1 
                     #statement 2 
                    # ...........
                    # statement n 
percents = [85.5,81.0,86.0,83.5]
for p in percents :
    print(p)

# for loop in str 
s1 = "HELLO WORLD"
for char in s1:
    print(char)

# for loop in dict
employee = {"empid":1001,"name":"john gray","department":"HR"}
for i in employee:
    print(i,employee[i])

# range() => it is built in function used to generate sequence of intervals in a given int and have (start,stop,steps).
# syntax = range(start,stop,step) 
# if steps are not given then it will +1 default and if start is not given then the 0 will bew the start but stop will be given for ending the loop.
profits = [9,11,6,10]
for index in range(len(profits)):
    q = index + 1 
    print(f"Profit for quater {q} is {profits[index]}")

# total , height and lowest using loops 
scores = [2,45,101,10,25,36,69,45,0,1,0]
total = 0
for score in scores :
    total = total + score
print(f"Total runs scored by a team is {total}")

highest = scores[0]
for high in scores:
    if highest<high :
        highest = high
print(f"Highest score in team is {highest}")

lowest = scores[0]
for low in scores :
    if lowest > low :
        lowest = low
print(f"Lowest score in team is {lowest}")

# continue => it is used to skip the skip the loop when it is true and it again go for iteration 
for num in range(10):
    if num % 3 == 0:
        continue
    print(num)

# break => it is used to get out from the loop when it is true
for num in range (1,10):
    if num % 3 == 0:
        break
    print(num)
