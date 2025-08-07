# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true


class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        row = 0
        col = m - 1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 5


print(Solution().searchMatrix(matrix, target))