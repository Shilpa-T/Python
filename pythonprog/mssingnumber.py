"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Find the Missing Number

You are given a list of n-1 integers and these integers are in the range of 1 to n.
 There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.
"""

# remove dictionary and do it regular value
#dont use iterative property on Dictionary


"""
METHOD 1(Use sum formula)
Algorithm:

1. Get the sum of numbers
       total = n*(n+1)/2
2  Subtract all the numbers from sum and
   you will get the missing number.
"""

def getMissingNo(nums):
    n=len(nums)+1 # no of elements = len +1(missing element)
    total = (n*(n+1))/2
    return total -sum(nums)


"""
METHOD 2(Use XOR)

  1) XOR all the array elements, let the result of XOR be X1.
  2) XOR all numbers from 1 to n, let XOR be X2.
  3) XOR of X1 and X2 gives the missing number.
  """

# getMissingNoX takes list as argument
def getMissingNoX(nums):
    n = len(nums)
    x1 = nums[0] # For xor of all the elements in array
    x2 = 1 # For xor of all the elements from 1 to n+1
    for i in range(n):
        x1 ^= nums[i]
    for i in range(n+1):
        x2 ^= i
    return x1^x2

def missingNumberx(nums):

    i = range(4)
    res = sum(i) ^ sum(nums)
    return res



def missingNumber(nums):
    d =[]
    nums = sorted(nums)
    for each in nums:
        d.append(each)
    for i in range(len(nums)):
        if d[i+1] - d[i] >1:
            a=d[i]+1
            return a


nums = [1,4,2]
nums1=[9,6,4,2,3,5,7,0,1]

print missingNumber(nums)
print getMissingNo(nums)
print getMissingNoX(nums)

#print missingNumber(nums1)

#print missingNumberx(nums)