'''                                            ARRAY OF PRODUCTS
Write a function that takes in a non-empty array of integers and returns an array of the same
length, where each element in the output array is equal to the productof every other number in
the input array.
In other words, the value at output[i] is equal to the product of every number in the input array 
other than input[i].
Note that you're expected to solve this problem without using division.
'''


def arrayOfProducts(array):
    n=len(array)
    result=[1]*n
    left_product=1
    for i in range(n):
        result[i]*=left_product
        left_product*=array[i]
    right_product=1;
    for i in range(n-1,-1,-1):
        result[i]*=right_product
        right_product*=array[i]
    return result


'''
   SAMPLE INPUT:
array=[5, 1, 4, 2]
   SAMPLE OUTPUT:
[8, 40, 10, 20]
// 8 is equal to 1 * 4 * 2
// 40 is equal to 5 * 4 * 2
// 10 is equal to 5 * 1 * 2
// 20 is equal to 5 * 1 * 4       
'''
