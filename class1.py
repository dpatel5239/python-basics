                               #**string topic in python**
s1 = " hello world" # string is a sequence of characters enclosed in single quotes, double quotes or triple quotes 
s2 = 'hello'
s3 = """hello world python """
s4 = "python "

print(len(s1))#len function is used to find the length of the string  
print(len(s2))
print(len(s3))
print(len(s4))

print(s2[0]) # indexing is used to access the individual characters of the string from the beginning of the string to the end
print(s2[1])
print(s2[2])
print(s2[3])
print(s2[4])

print(s2[-1]) # negative indexing is used to access the characters from the end of the string to the beginning
print(s2[-2])   
print(s2[-3])
print(s2[-4])   
print(s2[-5])  

print(s1+s4) # concatenation is used to combine two or more strings together without any space in between
print(s1+" "+s4) # concatenation with space in between 