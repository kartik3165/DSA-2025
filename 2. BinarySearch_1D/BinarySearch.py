arr = [1,2,3,4,5,6,7,8,9]


def bs(arr,target):
    low = 0
    high = len(arr) - 1

    while( low <= high):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def bsRecc(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return bsRecc(arr, target, low, mid - 1)
    else:
        return bsRecc(arr, target, mid + 1, high)


print(bsRecc(
    arr,
    6,
    0,
    (len(arr) - 1)
))
    





# print(bs(arr,4))
    

