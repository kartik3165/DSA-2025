def backtrack(path, nums, result, used):
    if len(path) == len(nums):
        result.append(path[:])
        return 
    
    for i in range(len(nums)):
        if used[i] == 0:
            path.append(nums[i])
            used[i] = 1
            backtrack(path, nums, result, used)
            used[i] = 0
            path.pop()

def print_per(nums):
    result = []
    used = [0] * len(nums)
    backtrack(
        [],
        nums,
        result,
        used
    ) 

    for i in result:
        print(i)