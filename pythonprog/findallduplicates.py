"""
Given an array of integers, 1 <= a[i] <=n (n = size of array),
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.

"""
Array_list =[]
dup_list = []
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
        dup_list.append(Array_list[num])
if count >=1:
    print "Elements appear twice",dup_list


