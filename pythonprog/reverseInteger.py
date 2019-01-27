"""
input = 123
output=321

"""
input = 123
input = str(input)
print input[::-1]


def reverse(input):

    pos = True
    d = 0
    if input < 0:
        pos = False
        input = -input
    while input !=0:
        d = d*10 + input%10
        input=input/10
    if not pos:
        return -d
    return d


input = 123
input1 = -321
input2 = 120
print reverse(input)
print reverse(input1)
print reverse(input2)