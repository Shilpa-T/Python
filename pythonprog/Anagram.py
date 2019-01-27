"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""


def isAnagram(s, t):
    """
    s = "anagram",t = "nagaram"
    :param s: string
    :param t: string
    :return:
    """
    if sorted(s)==sorted(t):
        return True
    else:
        return False


print isAnagram("anagram","nagaram")
print isAnagram("rat","car")
print isAnagram("shilpa","shilla")