def findprimenumber(list):
    """
    find the prime numebr in a list
    :param list:
    :return:
    """
    l =[]

    for num in list:
        if num >1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                l.append(num)
    return l

list = [1,3,6,7,8,11]

print findprimenumber(list)