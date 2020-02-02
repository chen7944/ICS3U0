#-----------------------------------------------------------------------------
# Name:        Exercise 05 (Lists) (exercise05.py)
# Purpose:     Execute multiple tasks instructed by teacher
#
# Author:      627944
# Created:     16-Oct-2019
# Updated:     16-Oct-2019
#-----------------------------------------------------------------------------

# don't touch this list, make your own!
preMadeList = ['5', '8', '6']

# declaring variables
aList = []
aString = ""

# task 1
aList.append(input())
while aList[-1] != "0":
    aList.append(input())
del aList[-1]
print(aList)

# task 2
del aList[2]
del aList[-1]
print(aList)

# task 3
print(aList[0:2])
print(aList[3:8])

# task 4
aList.sort()
for i in range(0, len(aList), 1):
    aString += aList[i]
print(aString)

# task 5
aList += preMadeList
print(aList)

# task 6
if input() in aList:
    print("YES")

# task 7
if input() not in aList:
    print("NOT")

# task 8
for i in range(0, len(aList), 1):
	aList[i] += "!"
print(aList)

# task 9
aCopiedList = aList.copy()
aList.append("TEST")
aListOfLists = [aList, aCopiedList]
print(aListOfLists)
