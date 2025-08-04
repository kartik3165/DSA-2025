# find nth root 3underroot4 = 1 * 3


def power(x, n):
    ans = 1
    for _ in range(1, n + 1):
        ans = ans * x
    return ans


def _nthRoot(n, nums):
    low = 1 
    high = nums
    while low <= high:
        mid = (low + high) // 2
        mid_power = power(mid,n)
        if mid_power == nums:
            return mid
        elif mid_power < nums:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(_nthRoot(3,27))

