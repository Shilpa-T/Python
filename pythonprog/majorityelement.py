"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ( n/2 ) times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""

def majorityElement(nums):
    """

    :param nums:
    :return:
    """
    j=len(nums)
    d = {}
    for each in nums:
        d[each]=d.get(each,0)+1
    for i,v in d.items():
        if v >=j/2:
            return i



num=[1,2,3,4,2,3,2,2,2,-1]
num1=[7, 7, 5, 7, 5, 1 , 5, 7 , 5, 5, 7, 7 , 7, 7, 7, 7]

print "Majority element",majorityElement(num)
print "Majority element",majorityElement(num1)