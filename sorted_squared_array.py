'''                             SORTED SQUARED ARRAY
Write a function that takes in a non-empty array of integers that are sorted in ascending
order and returns a new array of the same length with the squares of the original integers
also sorted in ascending order.
'''



def sortedSquaredArray(array):
  squared_array=[num**2 for num in array]
  squared_array.sort()
  return squared_array
  
''' SAMPLE INPUT
array=[1,2,3,5,6,8,9]
    SAMPLE OUTPUT
array=[1,4,9,25,36,64,81]    
'''
