import sqlite3
import re

def searchUser(field, searchTerm):
    """
	Searches for the user by their username
	:param username: The username that is trying to be found
	:return: A tuple of the record data of the user that matches with the record's username
    """
    # Connecting to sqlite
    conn = sqlite3.connect('db.sqlite3')
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

	# Retrieving data using the username 
    query = f"SELECT id, userName, userScore, userEmail, userPw, role FROM tracks WHERE {field} LIKE '{searchTerm}'"
    result = cursor.execute(query).fetchall()

	# Closing the connection
    conn.close()
    return result

def usernameAlreadyExists(username) -> bool:
	"""
	Checks if the username is already in the database
	:param username: The username that is trying to be found
	:return: True if username is found otherwise False
	"""
	return not len(searchUser('userName', username)) == 0

def presenceCheck(txtinput) -> bool:
    """
    Checks if anything is present in the data
    :param txtinput: The data that presence check is performed on
    :return: False if nothing is present in the string ("") otherwise return True
    """
    if txtinput:
        return True
    else:
        return False

def twoStringsMatchCheck(txtinput1, txtinput2) -> bool:
    """
    Checks if the 2 strings match
    :param txtinput1: The data will be checked if it matches with txtinput2
    :param txtinput2: The data will be checked if it matches with txtinput1
    :return: True if both txtinput1 and txtinput2 are the same otherwise False
    """
    return txtinput1 == txtinput2

def passwordComplexityCheck(username, password) -> bool:
    """
    Checks if the password:
    Contains at least 1 uppercase letter, lowercase letter, digit, and special character
    Does not contains username
    :param username: The username of the user's password that is being checked
    :param password: The password that is being checked if it is strong
    """
    # The password does not (contains at least 1 uppercase letter, lowercase letter, digit, and special character)
    if not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[_@$]" , password):
        return False
    elif re.search("\s" , password):
        return False

    # If the username is in the password
    if username in password:
        return False
    
    # All checks have been passed
    return True

def lengthAtLeastCheck(txtinput, lengthAtLeast) -> bool:
    """
    Checks if the length of the txtinput string is equal or bigger than lengthAtLeast integer
    :param txtinput: The string that is being checked
    :param lengthAtLeast: The minimum length of the txtinput string should be
    :return: True if the length of the txtinput string is equal or bigger than lengthAtLeast integer
    """
    # If the length of the txtinput is equal or bigger than lengthAtLeast
    if len(txtinput) >= lengthAtLeast:
        return True
    else:
        return False

def strongPasswordCheck(username, password) -> bool:
    """
    Checks if the password passes the length and complexity standards
    :param username: The username of the user's password that is being checked
    :param password: The password that is being checked if it is strong
    :return: True if the password has passed all the checks otherwise False
    """
    # Both checks have passed
    return passwordComplexityCheck(username, password) and lengthAtLeastCheck(password, 8)
