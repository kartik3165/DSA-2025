class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        index = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        
        if index == -1:
            nums.reverse()
            return nums
        
        for j in range(len(nums) - 1, index - 1, -1):
            if nums[j] > nums[index]:
                nums[j], nums[index] = nums[index], nums[j]
                break
        nums[index+1:] = reversed(nums[index+1:])
        return nums
    

arr = [1,2,3]

print(Solution().nextPermutation(arr))
