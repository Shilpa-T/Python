def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    list=[]
    tokens = []
    tokens = tokens +s.split()
    for token in tokens:
        token=token[::-1]
        list.append(token)
        print list


s="shilpa pujari"
reverseWords(s)