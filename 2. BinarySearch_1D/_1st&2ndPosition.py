# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution(object):
    def lowerBound(self,n,k):
        ans = 0
        low = 0
        high = len(n) - 1
        while low <= high:
            mid = (low + high) // 2
            if n[mid] >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def upperBound(self,n,k):
        ans = 0
        low = 0
        high = len(n) - 1
        while low <= high:
            mid = (low + high) // 2
            if n[mid] > k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def searchRange(self, nums, target):
        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)
        
        # Check if target exists at lb index
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        return [lb, ub - 1]

    

nums = [5,7,7,8,8,10]

    
print(
    Solution().searchRange(nums,8)
)
    

        
        