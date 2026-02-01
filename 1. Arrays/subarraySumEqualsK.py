from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        mpp = defaultdict(int)
        mpp[0] = 1
        count = 0
        preSum = 0

        for num in nums:
            preSum += num
            remove = preSum - k
            count += mpp[remove]
            mpp[preSum] += 1
        
        return count
    
def subarraySum(nums, k):
    mp = {0 : 1}
    count = 0
    preSum = 0

    for n in nums:
        preSum += n
        if preSum - k in mp:
            count += mp[preSum - k]
        mp[preSum] = mp.get(preSum, 0) + 1
    
    return count

nums = [1,1,1]
k = 2

print(subarraySum(nums, k))

# print(Solution().subarraySum(nums, k))