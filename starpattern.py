####################################### star pattern ######################################################
#1) lift triangle 
for i in range (1,6):
    for j in range (i):
        print("*",end=" ")
    print()

print()


#2) square pattern
for i in range (6):
    for j in range (6):
        print("*",end=" ")
    print()

print()

#3) inverted trinagle 
for i in range(5,0,-1):
    for j in range (i):
        print("*",end=" ")
    print()

print()

#4) pyramid pattern
for i in range (1,6):
    for j in range (6-i):
        print(" ",end=" ")
    for k in range (2*i-1):
        print("*",end = " ")
    print()

print()

#5) inverted pyramid 
for i in range (6,0,-1):
    for j in range (6-i):
        print(" ",end= " ")
    for k in range (2*i-1):
        print("*",end = " ")
    print()

print()

#6) diamond pattern 
for i in range(1,6):
    for j in range(6-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

for i in range(6,0,-1):  
    for j in range(6-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

print()
