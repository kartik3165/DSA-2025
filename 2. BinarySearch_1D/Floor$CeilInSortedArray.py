

def Cell(arr,k):
    ans = -1
    low =  0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < k:
            ans = arr[mid] 
            low = mid + 1
        else:
            high = mid - 1