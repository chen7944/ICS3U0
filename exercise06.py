#-----------------------------------------------------------------------------
# Name:        Exercise 06 (Functions) (exercise06.py)
# Purpose:     Execute multiple functions that return calculations
#
# Author:      627944
# Created:     18-Oct-2019
# Updated:     19-Oct-2019
#-----------------------------------------------------------------------------

def convertCToF(temperature):
  if temperature < -100 or temperature > 100:
    return "Unacceptable input values."
  return int(temperature * (9/5) + 32)
  
def convertFToC(temperature):
  if temperature < -100 or temperature > 100:
    return "Unacceptable input values."
  return int((temperature - 32) * (5/9))

def hypotenuse(a, b):
  if a <= 0 or b <= 0:
    return "Unacceptable input values."
  return (a**2 + b**2) ** 0.5
  
def milesToKm(distance):
  if distance <= 0:
    return "Unacceptable input values."
  return round((distance * 1.609), 2)
