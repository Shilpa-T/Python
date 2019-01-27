"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums,target):
    """

    :param nums: list of values
    :param target: value
    :return:
    """

    result=[]
    d = {}
    for i,v in enumerate(nums):
        if v in d:
            result.append((d[v],i))
        d[target-v] = i
    return result

nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [2,8,7,5,1,3,13,-3]
target2 = 10
print twoSum(nums1,target1)
print twoSum(nums2,target2)

