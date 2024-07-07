#!/usr/bin/python3
"""
A function that finds the peak value of the a list of values

"""

def find_peak(list_of_integers):
    """
    We will test for an empty list if we have encountered an 
    empty list we will return None
    """
    if list_of_integers == []:
        return None
    """
    We will need to find the length of integers to test against the
    minimum constraints which we may encounter for values between
    zero and two.
    """
    list_size = len(list_of_integers)
    if list_size == 0:
        return (None)
    elif list_size == 1:
        return (list_of_integers[0])
    elif list_size == 2:
        return max(list_of_integers)
    """
    We may encounter multi-peak values in our list of integers so therefore a loop
    will not work well, we will need to find the mid-point of the value and work our
    way to the left of the values or to the right of our mid to find the peak which is larger
    than both neighbors.
    """
    mid = int(list_size / 2)
    peak = list_of_integers[mid]
    my_list = list_of_integers
    """
    If we have found the peak value at the middle of the list we will return thte middle value,
    otherwise we will have to use recursion to evaluate the values to the right and the values to the left.
    """

    if peak > my_list[mid - 1] and peak > my_list[mid + 1]:
        return peak
    elif peak < my_list[mid - 1]:
        return find_peak(my_list[:mid])
    else:
        return find_peak(my_list[mid:])


