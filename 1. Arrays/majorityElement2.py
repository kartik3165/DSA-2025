class Solution(object):
    def majorityElement(self, nums):
        c1, c2 = 0,0
        e1, e2 = float('inf'),float('inf')

        for i in range(len(nums)):
            if c1 == 0 and nums[i] != e2:
                c1 = 1
                e1 = nums[i]
            elif c2 == 0 and nums[i] != e1:
                c2 = 1
                e2 = nums[i]
            elif nums[i] == e1:
                c1 += 1
            elif nums[i] == e2:
                c2 += 1 
            else:
                c1 -= 1
                c2 -= 1
        
        # return e1, e2
        if c1 == c2:
            return e1, e2
        else:
            if c1 > c2:
                return e1
            else:
                return e2
        


nums = [[3,2,3],[1], [1,2]]


for i in nums:
    print(Solution().majorityElement(i))