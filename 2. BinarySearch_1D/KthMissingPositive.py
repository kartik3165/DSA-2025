# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


class Solution(object):
    def findKthPositive(self, arr, k):
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k
        