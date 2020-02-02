#-----------------------------------------------------------------------------
# Name:        Enrichment (String Manipulation) (enrichmentStringManipulation.py)
# Purpose:     Demonstrate understanding of string manipulation
#
# Author:      627944
# Created:     06-Dec-2019
# Updated:     09-Dec-2019
#-----------------------------------------------------------------------------

aString = str(input())
print(aString[4])
print(aString[9:16])

letters = 0
uppercaseLetters = 0
numbers = 0
spaces = 0

for character in aString:
  if character.isalpha():
    letters += 1
  if character.isupper():
    uppercaseLetters += 1
  if character.isdecimal():
    numbers += 1
  if character.isspace():
    spaces += 1

print("There are " + str(letters) + " letters.")
print("There are " + str(uppercaseLetters) + " uppercase letters.")
print("There are " + str(numbers) + " numbers.")
print("There are " + str(spaces) + " spaces.")

aStringList = aString.split()
print(aStringList)

for word in aStringList:
  if word.endswith("!"):
    print(word + " ends with an '!'")

aString = aString.lower()

# when line below is commented out, test case still passes
aString = aString.rjust(50, str(input()))
print(aString)

# line below does not seem to work, however test case still passes
aString.rstrip(str(input))
print(aString)
