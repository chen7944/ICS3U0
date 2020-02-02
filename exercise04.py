#-----------------------------------------------------------------------------
# Name:        Exercise 04 (Loops) (exercise04.py)
# Purpose:     Simple Python program using print() and input()
#
# Author:      627944
# Created:     15-Oct-2019
# Updated:     15-Oct-2019
#-----------------------------------------------------------------------------

# declaring variables
total = 0
check = 0

# calculating sum until -1
while True:
  check = int(input())
  if (check == -1):
    break
  else:
    total += check

# prints "*" i times until total sum reached
for i in range(0, total, 1):
  print("*" * i)
