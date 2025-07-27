def containsDuplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
        
nums = [2,14,18,22,22]

print(containsDuplicate(nums))

