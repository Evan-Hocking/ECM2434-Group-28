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