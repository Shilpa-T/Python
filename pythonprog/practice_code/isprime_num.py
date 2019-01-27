def isprimenumber(num):
    """
    check whether number is prime number
    A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
    2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
    But 6 is not prime (it is composite) since, 2 x 3 = 6.
    :param number:
    :return:
    """

    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print num,"is not prime number"
                print i,"times",num//i,"is",num
                break
        else:
            print num,"is prime number"
    else:
        print num,"is not prime number"


isprimenumber(3)
isprimenumber(2)
isprimenumber(4)
isprimenumber(7)