#-----------------------------------------------------------------------------
# Name:        Exercise 03 (Conditionals) (exercise03.py)
# Purpose:     Receive input, and output based on if conditionals
#
# Author:      627944
# Created:     09-Oct-2019
# Updated:     09-Oct-2019
#-----------------------------------------------------------------------------

# declaring input variable
realNumber = int(input())

# check conditionals to determine appropriate output
if realNumber <= 0:
  print("Small")
elif realNumber > 100:
  print("Extremely Large")
else:
  print("Large")
