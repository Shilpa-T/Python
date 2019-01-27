"""
Given two arrays, write a function to compute their intersection.
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
Note:
Each element in the result must be unique.
The result can be in any order.
"""

#output should contain duplicates value(intersectin)

def intersection(nums1, nums2):
    """

    :param nums1:
    :param nums2:
    :return:
    """
    l=[]
    A = set(nums1)
    B = set(nums2)
    l=list(A&B)
    return l


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3=[-1,2,-3,-4,5,6]
nums4 = [-4,2,6,6]
print intersection(nums1, nums2)
print intersection(nums3, nums4)