# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        
        low = 0
        high =  (n * m - 1)

        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            print(f'row = {row}, col = {col} ')
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 3

print(Solution().searchMatrix(matrix, target))