def max_end3(nums):
    n = 0
    if nums[0] > nums[len(nums) - 1]:
        n = nums[0]
        print n
    else:
        n = nums[len(nums) - 1]
        print n
    for i in range(len(nums)):
        nums[i] = n
        print nums
    return nums


#print max_end3([11, 5,9])


def sum2(nums):
  sum=0
  if len(nums) <=2 and len(nums)!=0:
    for i in range(len(nums)-1):
        sum+=nums[i]
  elif len(nums)>2:
    sum+=nums[0]+nums[1]
  else:
    sum=0
  return sum

#print sum2([1, 2, 3])


def make_ends(nums):
  n=[]
  if len(nums)>=1:
      n.append(nums[0])
      n.append(nums[len(nums)-1])
      return n

#print make_ends([1, 2, 3])


def big_diff(nums):
    x=0
    y=0
    for i in range(len(nums)-1):
        x=max(nums[i],nums[i+1])
    return x

#print big_diff([10, 3, 5, 6])


def sum13(nums):
    sum=0
    for i in range(len(nums)):
        if nums[i]==13:
            i+=2
            print 'i',i
            continue
        else:
            sum+=nums[i]
            print nums[i],i
    return sum

print sum13([1, 2, 13, 2, 1, 13])


def sum(a,b):
    return a+b

print sum(15061 ,11749)