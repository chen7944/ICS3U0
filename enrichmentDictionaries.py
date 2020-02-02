#-----------------------------------------------------------------------------
# Name:        Enrichment (Dictionaries) (enrichmentDictionaries.py)
# Purpose:     Demonstrate understanding of dictionaries
#
# Author:      627944
# Created:     28-Nov-2019
# Updated:     28-Nov-2019
#-----------------------------------------------------------------------------

def addItem(groceryList, item, number):
  if item in groceryList.keys():
    groceryList[item] += number
  elif item not in groceryList.keys():
    groceryList[item] = number
  return groceryList

def deleteItem(groceryList, item):
  if item in groceryList.keys():
    del groceryList[item]
    return True
  elif item not in groceryList.keys():
    return False

def displayNames(groceryList):
  displayList = []
  for i in groceryList.keys():
    displayList.append(i)
  return displayList

def displayQuantity(groceryList):
  displayList = []
  valueTotal = 0
  for i in groceryList.values():
    displayList.append(i)
    valueTotal += i
  displayList.append(valueTotal)
  return displayList
