# list in python => it is the type of data type which use to collect the different data types in one variable within a square brakets []. 
student=["DIPAK", 21 , "b.tech"]
print(student)

#indexing list => the indexing of list also starts with the 0 and also the last element have a (-1) index no .
print(student[0])
print(student[-1])

# operation in list 

#1.slicing of the list => it is similar to the slicing of the string where we put the starting index , ending index and the gap .
# note =>  the ending element is not taken 
s1=["hello",56,"&",365,88,"dipak"]
print(s1[0:-1:2])

#2. concatenation of the list => it is also similar to the concentination of the string 
print(student+s1)

#3. repetition of the list => it is similar to the repetition of the string  where we use * and the num for the repetition 
print(student*3)

#4. append() => it is the function which is use to add the new element to the existing list at the ending .
#note => it can print directly in the print function because it make a changes in the existing list not make a new list like string .
s1.append("patel")
print(s1)

#5. insert() => it is similar to the append function but it add the element before the specified index . (at the argument index comes first then the new item)
s1.insert(1,"python")
print(s1)

#6. extend() => it is similar to the append function but it adds many new elements to the existing list 
l1=[98,48,68,58,28,38]
l1.extend([78,18,88])
print(l1)

#7 remove() => this function is used to remove the element from the existing list by simply writing the elemenet in the remove function 
l1.remove(58)
l1.remove(38)
l1.remove(28)
print(l1)

#8. pop() => it is similar to the remowe  function but insted of writing element we use index value which have to remove from the list 
student.pop(1)
print(student)

#9. reverse() => this function is used to reverse the list elements from one to last 
nums = [5,2,3,6,7,5,9,4,2]
nums.reverse()
print(nums)

#10. sort() => the sorting is used to arrange the numbers in an order normally ascending order is default 
number = [48,56,89,78,56,23,48,12,37]
number.sort()
print(number)
#note = sorting in descending order we have to write reverse = True
number.sort(reverse = True)
print(number)

#11. count() => this function is used to count the no of occurence of the particular element in the list 
print("The no of occurence of 5 in the list is :", nums.count(5))

#12. membership operation (in) => this operation is used to check the element is present in the list or not
          #(not in) => this is similar to the (in) member operation but gives the opposite answer   
print("DIPAK" in student)
print("DIPAK" not in student)


#nested list => we can also create list in an other list and so on 
l1 = [12,"dipak","$",55,[45,7,18,[10,1]]]
print( " the length of the l1 list is ", len(l1))
print(l1[-1][-1][-1])  

# shallow copy => it is the used to copy the elements of the one list to another list 
import copy
l1 = [25,"python",75.8,[1,2,3]]
l2 = copy.copy(l1)
#both l1 and have different memory address but same element address 
print(f"l1 => {l1},{id(l1)}")
print(f"l2 => {l2},{id(l2)}")
l1 [3][0] = 10
l1 [3][1] = 20
l1 [3][2] = 30
print(f"l1 => {l1},{id(l1)}")
print(f"l2 => {l2},{id(l2)}")

#deep copy => it is the used to get the different memoey location of the inner elements while cpoying from the one list to another 
