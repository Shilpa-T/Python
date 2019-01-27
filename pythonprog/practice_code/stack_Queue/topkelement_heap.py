
"""
Return top k elements
"""
import heapq

def topKelements(nums,K):
    h=[nums[0]]
    list = []
    for each in nums[1:]:
        if each > h[0] or len(h) < K:
            heapq.heappush(h,each)
        if len(h) > K:
            heapq.heappop(h)
    while K>0:
        list.append(heapq.heappop(h))
        K-=1
    return list[::-1]



num = [1,8,23,45,7,-4,90,6,37]

print (heapq.nlargest(3,num))
print (heapq.nsmallest(3,num))

list = topKelements(num,3)
print list