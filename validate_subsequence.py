'''             VALIDATE SUBSEQUENCE
Given two non-empty array of integers, write a function that determines whether
the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in
the array but that are in the same order as they appear in the array. For instance,
the numbers [1,3,4] form a subsequence of the array [1,2,3,4], and so do the numbers
[2,4]. Note that a single number in an array and the array itself are both valid subsequences 
of the array.
'''


def isValidSubsequence(array,subsequence):
  i,j=0,0
  while i<len(array) and j<len(subsequence):
    if array[i]==subsequence[j]:
      j+=1
    i+=1
  return j==len(subsequence)
  
  
'''
   SAMPLE INPUT
array=   [5,1,22,25,6,-1,8,10]
sequence=[1,6,-1,10]
   SAMPLE OUTPUT
true      
'''

