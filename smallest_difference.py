'''                       SMALLEST DIFFERENCE
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers
(one from each array) whose absolute difference is closest to zero, and returns an array containing
these two numbers, with the number from the first array in the first position.
Note that the absolute difference of two integers is the distance between them on the real number line.
For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.
'''


def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min_diff=float('inf')
    result_pair=[]
    i=j=0
    while i<len(arrayOne) and j<len(arrayTwo):
        current_diff=abs(arrayOne[i]-arrayTwo[j])
        if current_diff<min_diff:
            min_diff=current_diff
            result_pair=[arrayOne[i],arrayTwo[j]]
        if arrayOne[i]<arrayTwo[j]:
            i+=1
        elif arrayOne[i]>arrayTwo[j]:
            j+=1
        else:
            return result_pair
    return result_pair


'''
    SAMPLE INPUT
arrayOne=[-1,5,10,20,28,3]
arrayTwo=[26,134,135,1,17]
    SAMPLE OUTPUT
[28,26]        
'''
