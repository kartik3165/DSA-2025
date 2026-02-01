class Solution(object):
    def rearrangeArray(self, nums):
        ans = [0] * len(nums)
        posIndex = 0
        negIndex = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                ans[negIndex] = nums[i]
                negIndex += 2
            else:
                ans[posIndex] = nums[i]
                posIndex += 2
        return ans
    

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]

nums = [3,1,-2,-5,2,-4]

print(Solution().rearrangeArray(nums))
                



        