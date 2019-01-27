

"""
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
out=[1, 4, 3, 2, 0]
"""
def anagram_map(A,B):

    C = []
    for i in range(len(A)):
        C.append((B.index(A[i])))

    print C
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

anagram_map(A,B)

#anagram_map1(A,B)