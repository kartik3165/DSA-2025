def arrayUnion(arr1, arr2):
    l, r = 0, 0
    union = []

    while l < len(arr1) and r < len(arr2):
        while l > 0 and l < len(arr1) and arr1[l] == arr1[l - 1]:
            l += 1
        while r > 0 and r < len(arr2) and arr2[r] == arr2[r - 1]:
            r += 1
        if l >= len(arr1) or r >= len(arr2):
            break

        if arr1[l] < arr2[r]:
            union.append(arr1[l])
            l += 1
        elif arr1[l] > arr2[r]:
            union.append(arr2[r])
            r += 1
        else:  
            union.append(arr1[l])
            l += 1
            r += 1

    while l < len(arr1):
        if l == 0 or arr1[l] != arr1[l - 1]:
            union.append(arr1[l])
        l += 1

    while r < len(arr2):
        if r == 0 or arr2[r] != arr2[r - 1]:
            union.append(arr2[r])
        r += 1

    return union


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 7]

print(arrayUnion(arr1, arr2))  

