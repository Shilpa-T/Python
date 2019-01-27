"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

Array_list =[]
dup_list = []
count = 0
target = int(raw_input("enter target value"))
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
    if Array_list[num] + Array_list[num+1] == target:
        count = count +1
        dup_list.append(num)
        dup_list.append(num+1)
print "Elements indices",dup_list