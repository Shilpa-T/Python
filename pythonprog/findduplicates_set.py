"""
Given an array of integers, 1 <= a[i] <=n (n = size of array),
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.

"""


def findDuplicates(nums):
    """
    this function returns list of duplicate elements.
    :param nums:
    :return: list of duplicate elements
    """
    a_set = set()
    b_list = set()
    for i in nums:
        if i in a_set:
            b_list.add(i)
        else:
            a_set.add(i)
    return b_list

nums = [5,3,2,5,6,2,1,2]
print findDuplicates(nums)