# Input: n = 10, arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10], k = 9
# Output: 0.50000
# Explanation:
# One of the possible ways to place 10 gas stations is [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10].
# Thus the maximum difference between adjacent gas stations is 0.5.
# Hence, the value of dist is 0.5.
# It can be shown that there is no possible way to add 10 gas stations in such a way that the value of dist is lower than this.

# Input : n = 10, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1
# Output: 1.00000
# Explanation:
# One of the possible ways to place 1 gas station is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
# New Gas Station is at 11.
# Thus the maximum difference between adjacent gas stations is still 1.
# Hence, the value of dist is 1.
# It can be shown that there is no possible way to add 1 gas station in such a way that the value of dist is lower than this.

class Solution:
    def minimiseMaxDistance(self, arr, k):
        pass 