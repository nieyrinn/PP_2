#Ex 1
#Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Ex 2
#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Ex 3
#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Ex 4
#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Ex 5
#To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Ex 6
#Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
