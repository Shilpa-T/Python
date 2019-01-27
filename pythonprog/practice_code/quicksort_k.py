import quicksort as qs

def quicksort_k(arr,k):
    pi_value = qs.partition(arr,0,len(arr)-1)
    print pi_value
    while pi_value !=k-1:
        if pi_value >k-1:
            return quicksort_k(arr[:pi_value],k)
        else:
            return quicksort_k(arr[pi_value+1:], k)

    if pi_value ==k-1:
        return arr[0:k]

arr1=[8,3,6,2,1,0,5,7,4]

print quicksort_k(arr1,4)