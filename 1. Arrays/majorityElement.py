def majorityElement(nums):
        count = 0
        res = 0
        for i in range(len(nums)):
            if count == 0:
                res = i
            if nums[i] == nums[res]:
                count += 1
            else:
                count -= 1
        
        return nums[res]


print(majorityElement(nums = [2,2,1,1,1,2,2]))