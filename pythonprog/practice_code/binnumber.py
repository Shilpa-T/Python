def finonesinBinnum(num):
    """

    :param num:
    :return:
    """
    count=0
    num=bin(num)
    print num
    for i in num:
        if i == bool(1):
            count=count+1
    return count


print finonesinBinnum(2)