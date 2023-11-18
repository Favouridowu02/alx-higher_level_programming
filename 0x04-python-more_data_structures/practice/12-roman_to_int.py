#!/usr/bin/python3
def roman_to_int(roman_string):
    """ a function that converts a Roman numeral to an integer.

    Arguments:
        roman_string: the roman numeral to be cnverted

    Return: returns the integer value
    """
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    initial = 0

    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in roman_string:
        num += my_dict[i]
        if initial < my_dict[i]:
            num -= (initial * 2)
        initial = my_dict[i]
    return num
