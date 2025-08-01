def maxSubArray(self, nums):
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(currSum, maxSum)
        return maxSum