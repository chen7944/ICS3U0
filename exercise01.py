#-----------------------------------------------------------------------------
# Name:        Exercise 01 (Print, Math, Conversion) (exercise01.py)
# Purpose:     Show understanding of mathematical operations within Python
#
# Author:      627944
# Created:     07-Oct-2019
# Updated:     07-Oct-2019
#-----------------------------------------------------------------------------

# declaring int and float variables
intA = 5
intB = 7
floatA = 5.7
floatB = 7.5

# printing given tasks
print("this statement is printed to the terminal")
print(str(intA + intB))
print(str(floatB - floatA))
print(str(floatA * floatB))
print(str(intB / intA))
print(str(intB // intA))
print(str(intB % intA))
print(str(int(floatA)))
print(str(float(intA)))

# intA + intB = 2, intB % intA = 2, floatA * floatB = 42.75, 2 / 7 = 0.2857142857142857, 0.2857142857142857 // 2 = 0.0, 42.75 - 0.0 = 42.75, int(42.75) = 42
print(str(int(floatA * floatB - (intA + intB) / intB // (intB % intA))))
