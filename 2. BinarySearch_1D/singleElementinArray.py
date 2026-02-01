# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


class Solution(object):
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
                
        return nums[low]


nums = [1,1,2,3,3,4,4,8,8]

print(Solution().singleNonDuplicate(nums))
