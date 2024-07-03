#Two Number Sum In Python

def twoNumberSum(array, targetSum):
    seen_numbers=set()
    for num in array:
        complement=targetSum-num
        if complement in seen_numbers:
            return [complement,num]
        seen_numbers.add(num)
    return []
            
'''
Input [1,2,3]
Output: 6

'''