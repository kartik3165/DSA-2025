# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

# Example 2:
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4

# Example 3:
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1


class Solution(object):
    def _noOfDayReq(self, arr, limit):
        day = 0 
        weight = 0
        for i in range(len(arr)):
            if (weight + arr[i]) <= limit:
                weight += arr[i]
            else:
                weight = arr[i]
                day += 1
        return day
     
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self._noOfDayReq(weights, mid) < days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

weights = [1,2,3,4,5,6,7,8,9,10]

days = 5

print(Solution().shipWithinDays(weights, days))

        