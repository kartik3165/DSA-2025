class Solution(object):
    def twoSum(self, nums, target):
        j = 0
        for i in range(len(nums)):
            print(f'j = {nums[j]} and i = {nums[i]}')
            sums = nums[j] + nums[i]
            if i == len(nums) and sums != target:
                j += 1
            if sums == target:
                return [i,j]
            

        


nums = [2, 7, 11, 15]
n = [3,2,4]
t = 18

print(Solution().twoSum(nums, t))
