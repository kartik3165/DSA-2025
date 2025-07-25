class Solution(object):
    def maxSum(self, nums):
        max_element = max(nums)
        if max_element < 0:
            return max_element
        arr = []
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] not in arr:
                arr.append(nums[i])

        return sum(arr)


        