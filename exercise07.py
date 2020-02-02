#-----------------------------------------------------------------------------
# Name:        Exercise 07 (Docstrings) (exercise07.py)
# Purpose:     Execute multiple functions that return calculations, includes docstrings
#
# Author:      627944
# Created:     25-Nov-2019
# Updated:     25-Nov-2019
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
  if temperature < -100 or temperature > 100:
    return "Unacceptable input values."
  return int(temperature * (9/5) + 32)
  
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
  if temperature < -100 or temperature > 100:
    return "Unacceptable input values."
  return int((temperature - 32) * (5/9))

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
  if a <= 0 or b <= 0:
    return "Unacceptable input values."
  return (a**2 + b**2) ** 0.5
  
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
  if distance <= 0:
    return "Unacceptable input values."
  return round((distance * 1.609), 2)
