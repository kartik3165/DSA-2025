# find square root of number
# 25 = 5
# 38 = 6


def Sqrt(num):
    low = 1
    high = num
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= num:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans    


print(Sqrt(9))

