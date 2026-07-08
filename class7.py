                  #opeartions in string 
#repetatipon operation - use * after the string varible to and writer the times which you have to print              
n1 = "PATEL DIPAK"
n2 = "DIPAK PATEL"
s1 = " python is the fun "
print(n1*7)

#membership operation (in) - it is use to find the string or character is present or not and give the answer in boolean
print("PATEL " in n1)

#reverse membership operation (not in) - it is the opposite of the membership operation it gives false if the string is present and true when absent 
print("PATEL" not in n1)

#comparison of the string operation (==) - it is use to compare the two strings and give the answer in boolean 
print(n1 == n2)

#removing space operation (.strip()) - it is used to remove the blank spaces of the string from the starting and ending 
print(s1.strip())

#replacing operation (.replace("old string","new string",no of the times it should replace in multireplacing ))- this is used to replace the character or string from the present string .
print(s1.replace("the","not",1))

#counting operation (.count()) - it is used to count the no of occurencess of a string or character in the string 
print("The no of times \"p\" comes in the n1 =", n1.count("P"))

#changing the cases operations 
#upper() - it is used to convert all the characters of the string into upper cases not numeric or special 
print(n1.upper())
#lower() - it is used to convert all the characters of the string into lower cases 
print(n1.lower())
#title() - it is used to convert all words starting character into upper cases 
print(n1.title())
#capitalize() - it is used to convert only the first character into upper cases and others in lower cases of the string 
print(n1.capitalize())

# startswith() opeartion - it is used to check the first character of the string is similar to the given one or not 
print(n1.startswith("P"))
# endswith() - it is used to check the ending character is similar to the given one or not 
print(n1.endswith("k"))

