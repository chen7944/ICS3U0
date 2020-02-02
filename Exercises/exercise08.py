#-----------------------------------------------------------------------------
# Name:        Exercise 08 (Assertions) (exercise08.py)
# Purpose:     Execute multiple functions that return calculations, includes docstrings and assertions
#
# Author:      627944
# Created:     27-Nov-2019
# Updated:     27-Nov-2019
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
  String
    "Unacceptable input values."
  int
    fahrenheit from celcius' conversion.
  
  Warnings
  --------
  TypeError
    propogates when argument type is not correct
  NameError
    propogates when undefined variable is called

  Raises
  ------
  none
  '''
  
  assert isinstance(temperature, (int, float)), "Expecting 'temperature' to be an int or float"
	
  if temperature < -100 or temperature > 100:
    return "Unacceptable input values."
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
  String
    "Unacceptable input values."
  int
    celcius from fahrenheit's conversion.
  
  Warnings
  --------
  TypeError
    propogates when argument type is not correct
  NameError
    propogates when undefined variable is called

  Raises
  ------
  none
  '''
  
  assert isinstance(temperature, (int, float)), "Expecting 'temperature' to be an int or float"
  
  if temperature < -100 or temperature > 100:
    return "Unacceptable input values."
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
  String
    "Unacceptable input values."
  float
    hypotenuse of right-angled triangle with side lengths a and b
  
  Warnings
  --------
  TypeError
    propogates when argument type is not correct
  NameError
    propogates when undefined variable is called

  Raises
  ------
  none
  '''
  
  assert isinstance(a, (int, float)), "Expecting 'a' to be an int or float"
  assert isinstance(b, (int, float)), "Expecting 'b' to be an int or float"
  
  if a <= 0 or b <= 0:
    return "Unacceptable input values."
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
  String
    "Unacceptable input values."
  float
    kilometres from miles' conversion
  
  Warnings
  --------
  TypeError
    propogates when argument type is not correct
  NameError
    propogates when undefined variable is called

  Raises
  ------
  none
  '''
  
  assert isinstance(distance, (int, float)), "Expecting 'distance' to be an int or float"
  
  if distance <= 0:
    return "Unacceptable input values."
  return round((distance * 1.609), 2)

assert milesToKm(10) == 16.09, "Expecting 10 miles to equal 16.09 kilometres"
assert milesToKm(50) == 80.45, "Expecting 50 miles to equal 80.45 kilometres"
