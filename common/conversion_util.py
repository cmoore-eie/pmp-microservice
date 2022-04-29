"""
General functions used to convert information from one format to another
"""


def code_value(in_value):
    """
    Converts a string value to the format used to represent codes,
    spaces are removed and the string converted to lower case.
    :param in_value:
    :return: converted string or None if the input is not a string
    """
    if isinstance(in_value, str):
        ret_val = in_value.replace(' ', '').lower()
        return ret_val


def abbreviation_value(in_value):
    """
    Converts a string value to the format used to represent abbreviations,
    spaces are removed and the string converted to upper case.
    :param in_value:
    :return: converted string or None if the input is not a string
    """
    if isinstance(in_value, str):
        ret_val = in_value.replace(' ', '').upper()
        return ret_val
