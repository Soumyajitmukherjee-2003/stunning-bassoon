'''                        THREE NUMBER SUM
Write a function that takes in a non-empty array of distinct integers and an integer
representing a target sum. The function should find all triplets in the array that sum
up to the target sum and return a two-dimensional array of all these triplets. The numbers 
in each triplet should be ordered in ascending order, and the triplets themselves should be 
ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.
'''


def threeNumberSum(array, targetSum):
    array.sort()
    triplets=[]
    for i in range(len(array)-2):
        left,right=i+1,len(array)-1
        while left<right:
            current_sum=array[i]+array[left]+array[right]
            if current_sum==targetSum:
                triplet=[array[i],array[left],array[right]]
                triplets.append(triplet)
                left+=1
                right-=1
            elif current_sum<targetSum:
                left+=1
            else:
                right-=1
    return triplets     


'''
    SAMPLE INPUT
array=[12,3,1,2,-6,5,-8,6]
targetSum=0
    SAMPLE OUTPUT
[[-8,2,6],[-8,3,5],[-6,1,5]]        
'''
