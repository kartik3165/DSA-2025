# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[0]
        if nums[n-1] > nums[n-2]:
            return nums[n-1]
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


print(Solution().findPeakElement([1,2,1,3,5,6,4]))