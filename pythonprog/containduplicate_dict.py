"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

def containsDuplicate(nums):
    """
    This fuction finds duplicates in array.
    :param self:
    :param nums:
    :return: Boolean True or False
    """
    Max_occur = 0
    a_dict = {}
    for i in nums:
        a_dict[i]=a_dict.get(i,0)+1
    for k,v in a_dict.items():
        print k,v
        if v > 1:
            return True
    return False


nums = [1,2,9,4,3,9]
print containsDuplicate(nums)