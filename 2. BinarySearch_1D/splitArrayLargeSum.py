# Example 1:
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

class Solution(object):
    def _findGroup(self, arr, mid):
        group = 1
        min_sum = 0
        for i in range(len(arr)): 
            if (min_sum + arr[i]) <= mid:
                min_sum += arr[i]
            else:
                min_sum = arr[i]
                group += 1
        return group

    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self._findGroup(nums, mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans 


nums = [7,2,5,10,8]
n = [1,2,3,4,5]

# print(Solution()._findGroup(n, 9))
        
print(Solution().splitArray(n, 2))