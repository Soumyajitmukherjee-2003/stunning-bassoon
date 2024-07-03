def isValidSubsequence(array,subsequence):
  i,j=0,0
  while i<len(array) and j<len(subsequence):
    if array[i]==subsequence[j]:
      j+=1
    i+=1
  return j==len(subsequence)
  
  
'''
input:[1,2,3]
Output:[1,2],[2,3]
'''
