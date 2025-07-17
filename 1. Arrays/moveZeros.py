def moveZeroes(nums):
        left = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
        return nums



print(moveZeroes(nums = [0,1,0,3,12]))