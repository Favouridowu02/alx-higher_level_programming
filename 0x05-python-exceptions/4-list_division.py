#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ a function that divides element by element 2 lists.

    Argument:
        my_list_1: the first list
        my_list_2: the second list
        list_length: the number of elements to be printed out

    Return: new list (length = list_length) with all divisions
    """
    new_list = []
    i = 0

    while i < list_length:
        try:
            num = my_list_1[i] / my_list_2[i]
            new_list.append(num)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            i += 1
    return new_list
