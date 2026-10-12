# sets => it is the one of the mutable data type in which there is no indexing of the elements and they are enclosed in a curly braket {} without any repitions of any elements.

set_1 = {1,"dipak","$","hello",25,True}
print(type(set_1))

#basic operations in sets #

#1) add() => this function is used to add the new element to the set at a random place .
nums = {1,2,0,-1}
nums.add(3)
print(nums)

#2) remove()=> this function is used to get remove the element from the set permanantaly.
nums.remove(2)

#3) discard() => this function is similar to the remove function but it does not give any error if the removing element is absent in the sets
nums.discard(10)

#4) membship function (in , not in ) => this is used to check wether the given element is present in the sets or not 
print(0 in nums )
print(10 in nums)

#5) intersection () or & => this function is used to get the common elements from the two variables 
student1 = {"maths","english","chemistry","physics"}
student2 = {"maths","english","gk","cs","physics"}
common_subjects = student1 & student2
print(common_subjects)

#6) union () or (|) => this function is used to get the all elements from the variables
all_subjects = student1.union(student2)
print(all_subjects)

#7) diffrence of sets => this function is used to get the difference btw the sets
days = {"mon", "tue","wed","thur","fri","sat","sun"}
weekends = {"sat","sun"}
weekdays = days - weekends
print(weekdays)


#frozen sets => this is the another type of set which immutable so we can not do any add or remove function but can apply union or intersection .
fs1 = frozenset({10,20,30})
print(fs1,type(fs1))
