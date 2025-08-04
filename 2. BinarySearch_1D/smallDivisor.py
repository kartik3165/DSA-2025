# Example 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

# Example 2:
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
import math

class Solution(object):
    def thresholdSum(self, arr, num):
        total = 0
        for i in range(len(arr)):
            total += math.ceil(arr[i] / num)
        return total


    def smallestDivisor(self, nums, threshold):
        low = min(nums)
        high = max(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if self.thresholdSum(nums,mid) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
nums = [1,2,5,9]
th = 6

print(Solution().smallestDivisor(nums, th))
