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
    a_set = set()
    for i in nums:
        if i in a_set:
            return True
        else:
            a_set.add(i)
    return False



nums = [2,3,1,5,3,6,2,4]
value = containsDuplicate(nums)
print "Duplicates :",value