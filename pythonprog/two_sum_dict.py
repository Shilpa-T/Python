"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums,target):
    """
    Function returns the indices of numbers whose sum upto target value.
    :param nums: array of integers
    :param target: sum up value
    :return: Indices of two numbers
    """
    d_dict = {}
    result = []
    for i, v in enumerate(nums):
        if v in d_dict:
            #print d_dict[v], i
            result.append((d_dict[v],i))
        d_dict[target - v] = i
        #print d_dict
    return result



nums = [2, 7, 11, 15]
nums2 = [2,8,7,5,1,3,13,-3]
target = 10
print twoSum(nums2,target)