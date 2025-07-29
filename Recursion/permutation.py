def recur_permute(ds, nums, ans, freq):
    if len(ds) == len(nums):
        ans.append(ds[:])
        return
    
    for i in range(len(nums)):
        if not freq[i]:
            ds.append(nums[i])
            freq[i] = 1
            recur_permute(ds, nums, ans, freq)
            freq[i] = 0
            ds.pop()

def permute(nums):
    ans = []
    ds = []
    freq = [0] * len(nums)
    recur_permute(ds, nums, ans, freq)
    return ans

nums = [1, 2, 3]
print(permute(nums), end='')