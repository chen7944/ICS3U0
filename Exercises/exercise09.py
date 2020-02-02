#-----------------------------------------------------------------------------
# Name:        Exercise 09 (Exceptions) (exercise09.py)
# Purpose:     Execute multiple functions that return calculations, includes docstrings, assertions, and exceptions
#
# Author:      627944
# Created:     02-Dec-2019
# Updated:     02-Dec-2019
#-----------------------------------------------------------------------------

def convertCToF(temperature):
  '''
  Converts celcius to fahrenheit
  
  Takes in celcius as parameter temperature and returns the converted celcius as fahrenheit

  Parameters
  ----------
  temperature : int/float
    value of celcius (-100 <= temperature <= 100)
  
  Returns
  -------
  int
    fahrenheit from celcius' conversion.

  Raises
  ------
  TypeError
    if temperature is not an int or float
  ValueError
    if temperature is less than -100 or greater than 100
  '''
  
  if not isinstance(temperature, (int, float)):
    raise TypeError("Expecting 'temperature' to be an int or float")
  if temperature < -100 or temperature > 100:
    raise ValueError("Unacceptable input values.")
    
  return int(temperature * (9/5) + 32)
  
assert convertCToF(-40) == -40, "Expecting -40 degrees celcius to equal -40 degrees fahrenheit"
assert convertCToF(0) == 32, "Expecting 0 degrees celcius to equal 32 degrees fahrenheit"

def convertFToC(temperature):
  '''
  Converts fahrenheit to celcius
  
  Takes in fahrenheit as parameter temperature and returns the converted fahrenheit as celcius

  Parameters
  ----------
  temperature : int/float
    value of fahrenheit (-100 <= temperature <= 100)
  
  Returns
  -------
  int
    celcius from fahrenheit's conversion.

  Raises
  ------
  TypeError
    if temperature is not an int or float
  ValueError
    if temperature is less than -100 or greater than 100
  '''
  
  if not isinstance(temperature, (int, float)):
    raise TypeError("Expecting 'temperature' to be an int or float")
  if temperature < -100 or temperature > 100:
    raise ValueError("Unacceptable input values.")
    
  return int((temperature - 32) * (5/9))

assert convertFToC(-40) == -40, "Expecting -40 degrees fahrenheit to equal -40 degrees celcius"
assert convertFToC(0) == -17, "Expecting 0 degrees fahrenheit to equal -17 degrees celcius"

def hypotenuse(a, b):
  '''
  Calculates hypotenuse
  
  Takes in non-hypotenuse side lengths of right-angled triangle as parameters a and b then calculates and returns hypotenuse from arguments

  Parameters
  ----------
  a : int/float
    value of side length a (a >= 0)
  b : int/float
    value of side length b (b >= 0)
  
  Returns
  -------
  float
    hypotenuse of right-angled triangle with side lengths a and b

  Raises
  ------
  TypeError
    if a is not an int or float
    if b is not an int or float
  ValueError
    if a is less than or equal to 0 or b is less than or equal to 0
  '''
  
  if not isinstance(a, (int, float)):
    raise TypeError("Expecting 'a' to be an int or float")
  if not isinstance(b, (int, float)):
    raise TypeError("Expecting 'b' to be an int or float")
  if a <= 0 or b <= 0:
    raise ValueError("Unacceptable input values.")
    
  return (a**2 + b**2) ** 0.5
  
assert hypotenuse(3, 4) == 5, "Expecting non-hypotenuse sides 3 and 4 to have a hypotenuse of 5"
assert hypotenuse(5, 12) == 13, "Expecting non-hypotenuse sides 5 and 12 to have a hypotenuse of 13"

def milesToKm(distance):
  '''
  Converts miles to kilometres
  
  Takes in miles as parameter distance and returns the converted miles as kilometres

  Parameters
  ----------
  distance : int/float
    value of miles (distance >= 0)
  
  Returns
  -------
  float
    kilometres from miles' conversion

  Raises
  ------
  TypeError
    if distance is not an int or float
  ValueError
    if distance is less than or equal to 0
  '''
  
  if not isinstance(distance, (int, float)):
    raise TypeError("Expecting 'distance' to be an int or float")
  if distance <= 0:
    raise ValueError("Unacceptable input values.")
    
  return round((distance * 1.609), 2)

assert milesToKm(10) == 16.09, "Expecting 10 miles to equal 16.09 kilometres"
assert milesToKm(50) == 80.45, "Expecting 50 miles to equal 80.45 kilometres"

try:
  convertCToF(0)
  #convertCToF(101)
  convertFToC(0)
  #convertFToC(101)
  hypotenuse(3, 4)
  #hypotenuse('a', 'b')
  milesToKm(1)
  #milesToKm(0)
except (TypeError, ValueError) as e:
  print("Please Enter a Valid Input")
  print("Error Given: " + str(e))
