# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

import math

class Solution(object):
    def totalTime(self, n, piles):
        total = 0
        for i in range(len(piles)):
            total = total + math.ceil(piles[i] / n)
        return total


    def minEatingSpeed(self, piles, h):
        low = 1 
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if self.totalTime(mid, piles) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans



       

piles = [3,6,7,11]

print(Solution().minEatingSpeed(piles,8))

