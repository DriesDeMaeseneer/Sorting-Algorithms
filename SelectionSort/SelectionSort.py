#!/bin/python3

# This function searches the largest value of a given array.
def Largest(array):
    a = 0
    for i in array:
        # If a is smaller then i(current item from array), a=i.
        if a<i:
            a=i
    # Return the largest item.
    return a

# This function will return a sorted version of the array.
def SelectionSort(array):
    for i in range(len(array)):
        # Search the largest value in the array.
        # The slice([i:]) will remove the latest inserted b.
        a = Largest(array[i:])
        # Delete the item with the largest value
        b = array.pop(array.index(a))
        # Put the largest item in the front of the list
        array.insert(0,b)
        # return the array
    return array
