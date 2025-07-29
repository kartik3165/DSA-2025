def majorityElement(nums):
    count = 0
    elm = 0
    for i in range(len(nums)):
        if count == 0:
            elm = i
        if nums[elm] == nums[i]:
            count += 1
        else:
            count -= 1
    return nums[elm]

nums = [1,1,1,3,3,3,1,3,3]

print(majorityElement(nums))