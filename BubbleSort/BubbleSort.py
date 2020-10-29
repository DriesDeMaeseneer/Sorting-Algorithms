#!/bin/python3

def BubbleSort(array):
    """
    The function BubbleSort will sort an array with the bubble sort method.
    The return of the function is the sorted version of the array.
    """
    # Looping over all the items
    for i in range(len(array)-1):
        for j in range(len(array) - 1-i):
            # this if statement looks if the item on index i
            # bigger is then the next node.
            if array[j]>array[j+1]:
                # swap the items
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    # return the array
    return array
