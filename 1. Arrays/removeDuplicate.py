def removeDuplicates(nums):
        left = 1 
        for r in range(1, len(nums)):
            if nums[r - 1] != nums[r]:
                nums[left] = nums[r]
                left += 1
        
        return left

print(removeDuplicates(nums = [1,1,2,3,3,3]))