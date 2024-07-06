'''                                  MONOTONIC ARRAY
Write a function that takes in an array of integers and returns a boolean representing whether
the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing 
or entirely non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly,
non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
Note that empty arrays and arrays of one element are monotonic.
'''


def isMonotonic(array):
    increasing=decreasing=True
    for i in range(1,len(array)):
        if array[i]>array[i-1]:
            decreasing=False
        elif array[i]<array[i-1]:
            increasing=False
    return increasing or decreasing


'''
    SAMPLE INPUT
array=[-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
    SAMPLE OUTPUT
true    
'''
