"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
Array_list =[]
count = 0
while True:
    number = raw_input("enter the numbers(enter to quit) :")
    if not number:
        break
    number = int(number)
    Array_list.append(number)
    Array_list.sort()

print Array_list

for num in range(len(Array_list)-1):
    #print "num = ",num,"value :",Array_list[num],Array_list[num+1]
    if Array_list[num] == Array_list[num+1]:
        count = count +1
if count >=1:
    print "True"
else :
    print "False"


def findduplicate(input):
    """

    :param array:
    :return: Boolean True
    """
    a_dict = {}
    for





array =[4,6,3,3,5]
