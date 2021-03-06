"""
Given an array of integers, 1 <= a[i] <=n (n = size of array),
some elements appear twice or more and others appear once.
Find all the elements that appear heighest in this array.

"""


def findDuplicates(nums):
    """
    this function returns list of duplicate delement
    :param nums:
    :return: list of duplicate element
    """
    a_dict ={}
    l_list = []
    for i in nums:
        a_dict[i]=a_dict.get(i,0)+1
    for k,v in a_dict.items():
        if v >= max(a_dict.values()):
            l_list.append(k)
    return l_list

nums = [5,3,2,5,6,2,1,5]
print findDuplicates(nums)
