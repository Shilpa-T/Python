"""
A positive integer is called an Armstrong number of order n if
abcd... = an + bn + cn + dn + ...
In case of an Armstrong number of 3 digits, the sum of cubes of each digits is equal to the number itself.
For example:153
153=1*1*1+5*5*5+3*3*3

"""
def isArmstrong(num):
    """
    To find number is Armstrong number
    :param num:
    :return:
    """
    sum = 0
    temp = num
    order = len(str(temp))
    while temp>0:
        div=temp%10
        sum=sum+div**order
        temp=temp//10
    if num == sum:
        print num,"is Armstrong number"
    else:
        print num,"is not armstrong number"

isArmstrong(663)
isArmstrong(407)
isArmstrong(1634)