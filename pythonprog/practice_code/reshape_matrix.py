"""
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]
"""

def matrixReshape(nums, r, c):
    l=[]
    l=sum(nums,[])
    s=len(l)
    print l
    print s
    if r*c <= s:
        while r < range(len(l)):
            for c in range(len(l)):
                print "l",l[c]

    else:
        print "nums",nums

nums =[[1,2],
        [3,4]]

matrixReshape(nums,1,4)