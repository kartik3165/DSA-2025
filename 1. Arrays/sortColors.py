class Solution(object):
    def sortColors(self, nums):
        mid, low = 0,0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

nums = [2,0,1]

# output 1,0,2 but i want 0,1,2

print(Solution().sortColors(nums))