# Example 1:
# Input: mat = [[1,4],[3,2]]
# Output: [0,1]
# Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

# Example 2:
# Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
# Output: [1,1]
# Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.


class Solution(object):
    def findMaxElement(self, mat, n, m, col):
        maxElement = -1
        index = -1
        for i in range(n):
            if maxElement < mat[i][col]:
                maxElement = mat[i][col]
                index = i
        return index
    
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = low + high // 2
            rowIndex = self.findMaxElement(mat, n, m, mid)
            if mid - 1 >= 0:
                left = mat[rowIndex][mid - 1]
            else:
                left = -1
            if mid + 1 < m:
                right = mat[rowIndex][mid + 1]
            else:
                right = -1
            if mat[rowIndex][mid] > left and mat[rowIndex][mid] > right:
                return [rowIndex, mid]
            elif mat[rowIndex][mid] > left:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]
    

print(Solution().findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))