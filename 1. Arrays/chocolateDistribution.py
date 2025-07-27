def findMinDiff(arr,M):
    arr.sort()
    min_val = float('inf')
    for i in range(len(arr)):
        if (i + M - 1) < len(arr):
            val = arr[i + M - 1] - arr[i]
            if val < min_val:
                min_val = val
    return min_val

arr = [3, 4, 1, 9, 56, 7, 9, 12]

print(findMinDiff(arr,5))