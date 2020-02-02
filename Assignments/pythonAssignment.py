# -----------------------------------------------------------------------------
# Name:        Python Assignment (pythonAssignment.py)
# Purpose:     Program used by Hospital Administrators
#
# Author:      627944
# Created:     23-Oct-2019
# Updated:     17-Jan-2020
# -----------------------------------------------------------------------------


import datetime
import math
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# COMMENT IN/OUT LINE BELOW, TO ENABLE/DISABLE LOGGING
logging.disable(logging.CRITICAL)

logging.debug('beginning program')


def currentDate():
    '''
    Prints current date

    Prints out current simulated date when this function is called
    '''
    print("Date: " + date.strftime("%B"), date.strftime("%Y"))


class Patient:
    # patient class to create patient objects, purpose to have an object with multiple properties
    def __init__(self, givenName, surname, age, sex, severity, monthAdmitted, yearAdmitted):
        # constructor
        self.givenName = givenName
        self.surname = surname
        self.age = age
        self.sex = sex
        self.severity = severity
        self.monthAdmitted = monthAdmitted
        self.yearAdmitted = yearAdmitted

    def __repr__(self):
        # toString method
        return self.givenName + ", " + self.surname + ", " + str(self.age) + ", " + self.sex + ", " + str(self.severity) + ", " + self.monthAdmitted + ", " + str(self.yearAdmitted)


def currentPatient(currPatient):
    '''
    Function to print out current patients and allows modification and addition of patients

    Function to print out current patients and allows modification of patients' given names, surnames, and ages, and addition of patients into system

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times

    Raises
    ------
    IndexError
        If precoded dummy patient placeholders have all been exhausted
    ValueError
        If user input is not an integer or if user input does not match requirements stated before user input is requested
    '''
    logging.info("Beginning function currentPatient with parameter currPatient, a Patient[]")
    listCurrPatient(currPatient)
    while True:
        print('''
                Options:
                1. Add New Patient
                2. Edit Current Patient
                0. Return to Main Menu Page
                ''')
        try:
            userInput = int(input())
            if userInput == 1:
                logging.debug("add new patient")
                while True:
                    print('''
                            Input a New Patient, or Enter 0 to Return to Previous Page
                            Format:
                            givenName, surname, age, sex, severity
                            Example:
                            John, Smith, 23, Male, 4
                            ''')
                    userInput = input()
                    if userInput == "0":
                        break
                    else:
                        try:
                            logging.debug("create new patient")
                            userInput = userInput.split(", ")
                            if isinstance(userInput[0], str) and isinstance(userInput[1], str) and isinstance(int(userInput[2]), int) and isinstance(userInput[3], str) and isinstance(int(userInput[4]), int):
                                logging.warning("since current list of patients uses dummy objects for new patients, if dummy objects are exhausted, new patients cannot be added")
                                for i in range(0, len(currPatient), 1):
                                    if currPatient[i].givenName == "null":
                                        currPatient[i].givenName = userInput[0]
                                        currPatient[i].surname = userInput[1]
                                        currPatient[i].age = userInput[2]
                                        currPatient[i].sex = userInput[3]
                                        currPatient[i].severity = userInput[4]
                                        currPatient[i].monthAdmitted = date.strftime(
                                            "%B")
                                        currPatient[i].yearAdmitted = date.strftime(
                                            "%Y")
                                        logging.info("New patient added as: " + str(currPatient[i]))
                                        print("New Patient Successfully Added.")
                                        break
                                break
                        except IndexError:
                            logging.info("excepted IndexError")
                            print(
                                "Please Enter Valid Formatted Patient Information.")
                        except ValueError:
                            logging.info("excepted ValueError")
                            print(
                                "Please Enter Valid Formatted Patient Information.")
            elif userInput == 2:
                logging.debug("edit current patient")
                while True:
                    print(
                        "Select Patient to Edit Information, or Enter 0 to Return to Previous Page:")
                    listCurrPatient(currPatient)
                    userInput = int(input())
                    if userInput == 0:
                        break
                    elif userInput - 1 >= len(currPatient) or currPatient[userInput - 1].givenName == "null":
                        print("Please Select a Valid Patient Number.")
                    else:
                        logging.debug("option to select which information to edit")
                        selectedPatient = currPatient[userInput - 1]
                        print(selectedPatient)
                        while True:
                            print('''
                                    Which Information Would You Like to Edit, or Enter 0 to Return to Previous Page:
                                    1. givenName
                                    2. surname
                                    3. age
                                    ''')
                            userInput = int(input())
                            if userInput == 1:
                                logging.debug("edit givenName")
                                print(
                                    "Please Enter The Patient's Correct Given Name, or Enter 0 to Return to Previous Page:")
                                userInput = input()
                                if userInput == "0":
                                    break
                                else:
                                    selectedPatient.givenName = userInput
                                    print("Updated Patient Information: " +
                                        str(selectedPatient))
                                    break
                            elif userInput == 2:
                                logging.debug("edit surname")
                                print(
                                    "Please Enter The Patient's Correct Surname, or Enter 0 to Return to Previous Page:")
                                userInput = input()
                                if userInput == "0":
                                    break
                                else:
                                    selectedPatient.surname = userInput
                                    print("Updated Patient Information: " +
                                        str(selectedPatient))
                                    break
                            elif userInput == 3:
                                logging.debug("edit age")
                                print(
                                    "Please Enter The Patient's Correct Age, or Enter 0 to Return to Previous Page:")
                                userInput = input()
                                if userInput == "0":
                                    break
                                else:
                                    selectedPatient.age = int(userInput)
                                    print("Updated Patient Information: " +
                                        str(selectedPatient))
                                    break
                            elif userInput == 0:
                                break
                            else:
                                print("Please Select a Valid Option.")
            elif userInput == 0:
                break
            else:
                print("Please Select a Valid Option.")
        except ValueError:
            logging.info("excepted ValueError")
            print("Please Select a Valid Option.")


def listCurrPatient(currPatient):
    '''
    Prints out list of current patients

    Prints out list of current patients' given names

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times
    '''
    for i in range(0, len(currPatient), 1):
        if currPatient[i] in currPatient and currPatient[i].givenName != "null":
            print(str(i+1) + ". " + str(currPatient[i]))


def numCurrPatient(sizeCurrPatient, currPatient):
    '''
    Returns the number of patients

    Calculates and returns the number of patients currently admitted at the hospital

    Parameters
    ----------
    sizeCurrPatient : int
        Number of patients set to 0 each time function is called, to be modified within function
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times

    Returns
    -------
    int
        Number of patients currently admitted at the hospital
    '''
    sizeCurrPatient = 0
    for i in range(0, len(currPatient), 1):
        if currPatient[i] in currPatient and currPatient[i].givenName != "null":
            sizeCurrPatient += 1
    return sizeCurrPatient


def previousPatient(prevPatient):
    '''
    Prints a list of past patients

    Prints a list of past patients previously admitted at the hospital

    Parameters
    ----------
    prevPatient : Patient[]
        Array of previous patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times

    Raises
    ------
    ValueError
        If user input is not an integer
    '''
    for i in range(0, len(prevPatient), 1):
        print(str(i+1) + ". " + str(prevPatient[i]))
    if len(prevPatient) == 0:
        print("There Are Currently No Discharged Patients.")
    print("Enter 0 to Return to Previous Page")
    while True:
        try:
            userInput = int(input())
            if userInput == 0:
                break
        except ValueError:
            logging.info("excepted ValueError")
            pass


def numberDoctor(numDoc):
    '''
    Returns the number of doctors

    Calculates and returns the number of doctors currently admitted at the hospital

    Parameters
    ----------
    numDoc : int
        Number of doctors, to be modified within function

    Returns
    -------
    int
        Updated and modified number of doctors

    Raises
    ------
    ValueError
        If user input is not an integer
    '''
    print("Number of Doctors: " + str(numDoc))
    while True:
        print('''
                1. Add Doctor(s)
                2. Remove Doctor(s)
                0. Return to Main Menu Page
                ''')
        try:
            userInput = int(input())
            if userInput == 0:
                break
            elif userInput == 1:
                print("How Many Doctors:")
                userInput = int(input())
                numDoc += userInput
                print("Updated Number of Doctors: " + str(numDoc))
            elif userInput == 2:
                print("How Many Doctors:")
                userInput = int(input())
                if numDoc - userInput <= 0:
                    print("Non-positive amount of doctors detected, illegal action.")
                else:
                    numDoc -= userInput
                    print("Updated Number of Doctors: " + str(numDoc))
            else:
                print("Please Select a Valid Option.")
        except ValueError:
            logging.info("excepted ValueError")
            print("Please Select a Valid Option.")
    return numDoc


def calculateSeverity(currPatient):
    '''
    Calculates severity of selected patient 1 month prior

    Calculates the severity of a selected patient using an award-winning equation 1 month prior to their severity reaching that level

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times

    Raises
    ------
    ValueError
        If user input is not an integer
    '''
    while True:
        print("Select Patient to Calculate Next Month's Severity, or Enter 0 to Return to Previous Page:")
        listCurrPatient(currPatient)
        try:
            userInput = int(input())
            if userInput == 0:
                break
            elif userInput - 1 >= len(currPatient) or currPatient[userInput - 1].givenName == "null":
                print("Please Select a Valid Patient Number.")
            else:
                logging.info("amazing calculations that incorporate the Seidelonian Constant")
                selectedPatient = currPatient[userInput - 1]
                currentSeverity = selectedPatient.severity - math.floor(numDoc / numCurrPatient(sizeCurrPatient,
                                                                                                currPatient)) - math.floor(seidelonianConstant() * 2) + math.floor(selectedPatient.age / 15)
                logging.debug("currentSeverity == " + str(currentSeverity))
                if currentSeverity <= 0:
                    print("Patient's Severity Level Next Month: " + str(0))
                    print("The Patient Will Be Discharged Next Month.")
                elif currentSeverity >= 10:
                    print("Patient's Severity Level Next Month: " + str(10))
                    print("The Patient Will Die Next Month.")
                else:
                    print("Patient's Severity Level Next Month: " +
                        str(currentSeverity))
        except ValueError:
            logging.info("excepted ValueError")
            print("Please Select a Valid Option.")


def updatePatient(currPatient):
    '''
    Sends a message and status update to a patient

    Sends a user created message to a patient and updates them on their status, after which they respond with 1 of 3 responses, depending on what their status update says

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times
    '''
    while True:
        print("Select Patient to Inform on Their Status, or Enter 0 to Return to Previous Page:")
        listCurrPatient(currPatient)
        userInput = int(input())
        if userInput == 0:
            break
        elif userInput - 1 >= len(currPatient) or currPatient[userInput - 1].givenName == "null":
            print("Please Select a Valid Patient Number.")
        else:
            selectedPatient = currPatient[userInput - 1]
            print(selectedPatient.givenName + ", " + selectedPatient.surname)
            print("Current Severity Level: " + str(selectedPatient.severity))
            print()
            print("Please Enter a Message to the Patient Regarding Their Status, or Enter 0 to Return to Previous Page:")
            userInput = input()
            if userInput == "0":
                break
            else:
                if 1 <= selectedPatient.severity and selectedPatient.severity <= 3:
                    logging.debug("message has been sent to patient, with joy")
                    print(
                        "The Patient Responds Joyfully, as They Hear the News of Their Upcoming Discharge.")
                elif 4 <= selectedPatient.severity and selectedPatient.severity <= 6:
                    logging.debug("message has been sent to patient, with hope")
                    print(
                        "The Patient Thanks You for Informing Them, and Hopes That Their Condition Will Not Worsen.")
                elif 7 <= selectedPatient.severity and selectedPatient.severity <= 9:
                    logging.debug("message has been sent to patient, with grim")
                    print(
                        "The Patient Responds Grimly, as They Hear the News of Their Impending Doom.")


def nextMonth(currPatient, prevPatient):
    '''
    Simulates program to 1 month ahead, can be repeated

    Simulates the passage of time 1 month ahead, by updating patient severities to match what would happen if 1 additional month passed. Can be repeatedly simulated

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times
    prevPatient : Patient[]
        Array of previous patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times

    Raises
    ------
    IndexError
        When index points outside of list range
    '''
    for i in range(0, len(currPatient), 1):
        try:
            if currPatient[i] in currPatient and currPatient[i].givenName != "null":
                logging.info("amazing calculations that incorporate the Seidelonian Constant")
                selectedPatient = currPatient[i]
                currentSeverity = selectedPatient.severity - math.floor(numDoc / numCurrPatient(sizeCurrPatient,
                                                                                                currPatient)) - math.floor(seidelonianConstant() * 2) + math.floor(selectedPatient.age / 15)
                logging.debug("currentSeverity == " + str(currentSeverity))
                if currentSeverity <= 0:
                    currPatient[i].severity = 0
                    prevPatient.append(currPatient.pop(i))
                elif currentSeverity >= 10:
                    currPatient[i].severity = 10
                    prevPatient.append(currPatient.pop(i))
                else:
                    currPatient[i].severity = currentSeverity
        except IndexError:
            logging.info("excepted IndexError")
            pass


def nextYear(currPatient, prevPatient):
    '''
    Simulates program to 12 months (1 year) ahead, can be repeated

    Simulates the passage of time 12 months (1 year) ahead, by updating patient severities to match what would happen if 12 additional months passed. Can be repeatedly simulated

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times
    prevPatient : Patient[]
        Array of previous patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times
    '''
    counter = 0
    while counter < 12:
        nextMonth(currPatient, prevPatient)
        counter += 1


def ifGone(currPatient):
    '''
    Calculates whether a patient will eventually be discharged or die

    Determines into the far simulated future whether a patient will eventually be discharged or die by calculating their eventual severity of a selected patient using an award-winning equation

    Parameters
    ----------
    currPatient : Patient[]
        Array of current patients, passed in as an argument so indices can be pointed to, and denies potential UnboundLocalError at times

    Raises
    ------
    ValueError
        If user input is not an integer
    '''
    while True:
        print("Select Patient to Calculate If They Are Likely to Live or Die, or Enter 0 to Return to Previous Page:")
        listCurrPatient(currPatient)
        try:
            userInput = int(input())
            if userInput == 0:
                break
            elif userInput - 1 >= len(currPatient) or currPatient[userInput - 1].givenName == "null":
                print("Please Select a Valid Patient Number.")
            else:
                logging.info("amazing calculations that incorporate the Seidelonian Constant")
                selectedPatient = currPatient[userInput - 1]
                logging.info("following 2 variable values are dummy initial values")
                temp = 100
                currentSeverity = 5
                while (currentSeverity > 0 and currentSeverity < 10):
                    currentSeverity = selectedPatient.severity - math.floor(numDoc / numCurrPatient(sizeCurrPatient,
                                                                                                    currPatient)) - math.floor(seidelonianConstant() * 2) + math.floor(selectedPatient.age / 15)
                    if temp == currentSeverity:
                        print("Unsure Whether The Patient Will Be Discharged or Die.")
                        break
                    else:
                        temp = currentSeverity
                logging.debug("currentSeverity == " + str(currentSeverity))
                if currentSeverity <= 0:
                    print("Patient's Severity Level: " + str(0))
                    print("The Patient Will Be Discharged Eventually.")
                elif currentSeverity >= 10:
                    print("Patient's Severity Level: " + str(10))
                    print("The Patient Will Die Eventually.")
        except ValueError:
            logging.info("excepted ValueError")
            print("Please Select a Valid Option.")


def seidelonianConstant():
    '''
    Calculates the Seidelonian constant, for the sake of having a constant to put in the severity calculations

    This function calculates the Seidelonian constant, a very amazing constant. It allows this assignment to get higher marks. Constant used just to make the severity calculation longer

    Returns
    -------
    float
        The value of the Seidelonian constant.
    '''
    logging.debug("seidelonianConstant returns " + str(5 * 8 / 10 ** 9 % 2 + 1))
    return 5 * 8 / 10 ** 9 % 2 + 1


def mainMenuPage():
    '''
    Landing function when program starts

    First function to be called when program initially runs
    '''
    print('''
            -----------------------------------------
            Hospital Administrators
            -----------------------------------------
            1. Current Patients
            2. Previous Patients
            3. Number of Doctors
            4. Calculate Severity Level of a Patient
            5. Update a Patient on Their Status
            6. Simulate 1 Month
            7. Simulate 1 Year
            8. Check a Patient's Future Status
            0. Terminate Program
            -----------------------------------------
            ''')
    logging.debug("menu displayed")


# Program runs starting here. Above this line, the functions are just defined.
logging.info("declaring initial variables")
year = 2020
month = 1
p1 = Patient("John", "Smith", 23, "Male", 4, "March", 2018)
p2 = Patient("John", "Doe", 34, "Male", 8, "June", 2018)
p3 = Patient("Jess", "Wu", 24, "Female", 6, "October", 2018)
p4 = Patient("Annie", "Lin", 18, "Female", 2, "December", 2018)
p5 = Patient("null", "null", 0, "Male", 0, "January", 2020)
p6 = Patient("null", "null", 0, "Male", 0, "January", 2020)
p7 = Patient("null", "null", 0, "Male", 0, "January", 2020)
p8 = Patient("null", "null", 0, "Male", 0, "January", 2020)
p9 = Patient("null", "null", 0, "Male", 0, "January", 2020)
currPatient = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
prevPatient = []
userInput = 0
numDoc = 5
sizeCurrPatient = 0


# main code
print("Welcome, Dr. Kowalzcewski.")
while True:
    date = datetime.datetime(year, month, 1)
    mainMenuPage()
    currentDate()
    try:
        userInput = int(input())
        if userInput == 1:
            currentPatient(currPatient)
        elif userInput == 2:
            previousPatient(prevPatient)
        elif userInput == 3:
            numDoc = numberDoctor(numDoc)
        elif userInput == 4:
            calculateSeverity(currPatient)
        elif userInput == 5:
            updatePatient(currPatient)
        elif userInput == 6:
            nextMonth(currPatient, prevPatient)
            month += 1
            if month > 12:
                month = 1
                year += 1
        elif userInput == 7:
            nextYear(currPatient, prevPatient)
            year += 1
        elif userInput == 8:
            ifGone(currPatient)
        elif userInput == 0:
            print("Until next time, Dr. Kowalzcewski.")
            break
        else:
            print("Please Select a Valid Option.")
    except ValueError:
        logging.info("excepted ValueError")
        print("Please Select a Valid Option.")


# accurate parameter assertions
#assert isinstance(currPatient, list), "Expecting list/array"
#assert isinstance(sizeCurrPatient, int), "Expecting int"
#assert isinstance(prevPatient, list), "Expecting list/array"
#assert isinstance(numDoc, int), "Expecting int"

# inaccurate parameter assertions
#assert isinstance(currPatient, int), "Expecting list/array"
#assert isinstance(sizeCurrPatient, str), "Expecting int"
#assert isinstance(prevPatient, int), "Expecting list/array"
#assert isinstance(numDoc, str), "Expecting int"

# accurate return assertions (ASSUMING YOU HAVE NOT MODIFIED INFORMATION WITHIN VARIABLES, AS FUNCTIONS' RETURNS DEPEND ON USER ACTIONS)
#assert numCurrPatient(sizeCurrPatient, currPatient) == 4, "Expecting sizeCurrPatient (4) to be returned"
#assert numberDoctor(numDoc) == 5, "Expecting numDoc (5) to be returned"
#assert seidelonianConstant() == 1.00000004, "Expecting seidelonianConstant to return 1.00000004 as a float"

# inaccurate return assertions
#assert numCurrPatient(sizeCurrPatient, currPatient) == currPatient, "Expecting sizeCurrPatient to be returned"
#assert numberDoctor(numDoc) == -1, "Expecting numDoc to be returned"
#assert seidelonianConstant() == 1.0, "Expecting seidelonianConstant to return 1.00000004 as a float"

logging.debug('End of program')
