"""
Given an array of integers, find if the array contains any duplicates.
Your function should return trueif any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


def containsDuplicate(nums):
    d = {}
    for each in nums:
        d[each]=d.get(each,0)+1

    for i,v in d.items():
        #print i,v
        if v > 1:
            return True
    return False



nums = [4,3,2,5,6,7,2,8]
nums1=[-1,2,3,5,-1,2,8]
nums3 = [3,6,7,8,9,1]

print containsDuplicate(nums)
print containsDuplicate(nums1)
print containsDuplicate(nums3)
