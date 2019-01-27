
"""
Given an array of integers, 1 <= a[i] <=n (n = size of array),
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.

"""


def removeDuplicates(nums):
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
        if v > 1:
            l_list.append(k)
        else:
            l_list.append(k)
    return l_list

def removeduplicate(nums):
    s = []

    for i in nums:
        if i not in s:
            s.append(i)
    return s

#HW--write s code to remove duplicate in i/p list

def removeduplicates_ip(nums):

    nums = set(nums)
    return list(nums)


def removeduplicates_dict(nums):

    print dict.fromkeys(nums).keys()



nums = [5,3,2,5,6,2,1]
print removeDuplicates(nums)

print removeduplicate(nums)

print removeduplicates_ip(nums)

removeduplicates_dict(nums)


print "**************************************"
seq = [1,2,3,'a', 'a', 1,2]

print dict.fromkeys(seq).keys()


