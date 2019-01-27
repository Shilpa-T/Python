"""
arr =[ 2,3,6,4,1]
product_arry_except itself:
dont use divison

output :[72, 48,24, 36, 144 ]

"""

def prod_exitself(arr):
    """

    :param arr:
    :return:
    """
    size = len(arr)
    output = [1] * size
    left = 1
    for x in range(size - 1):
        left *= arr[x]
        output[x + 1] *= left
        print "a",output
    right = 1
    for x in range(size - 1, 0, -1):
        right *= arr[x]
        output[x - 1] *= right
        print "b",output
    return output


arr =[ 1,2,3,4]
arr1 =[ 2,3,6,4,1]
print prod_exitself(arr)
print prod_exitself(arr1)


