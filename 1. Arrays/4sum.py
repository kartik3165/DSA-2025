# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] and nums[j - 1]:
                    continue
                k = j + 1
                m = n - 1
                while k < m:
                    total = nums[i]+nums[j]+nums[k]+nums[m]
                    if total == target:
                        ans.append([nums[i],nums[j], nums[k], nums[m]]) # pyright: ignore[reportCallIssue]
                        while k < m and nums[k] == nums[k + 1]:
                            k += 1

                        while k < m and nums[m] == nums[m-1]:
                            m -= 1
                        k += 1
                        m -= 1
                    elif total < target:
                        k += 1
                    else:
                        m -= 1
                
                    

        return ans
    
nums = [1,0,-1,0,-2,2]
target = 0

print(Solution().fourSum(nums,target))

        