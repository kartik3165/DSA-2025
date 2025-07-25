def get_min_max(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr
    
arr= [3, 2, 1, 56, 10000, 167]

print(get_min_max(arr))