# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# class Solution(object):
#     def spiralOrder(self, matrix):
#         res = []
#         while matrix:
#             res += matrix.pop(0)

#             if matrix and matrix[0]:
#                 for row in matrix:
#                     res.append(row.pop())

#             if matrix:
#                 res += matrix.pop()[::-1]

#             if matrix and matrix[0]:
#                 for row in matrix[::-1]:
#                     res.append(row.pop(0))
#         return res

class Solution(object):
    def spiralOrder(self, matrix):
        element = []
        tl = 0
        bl = 0
        tr = len(matrix[0]) - 1
        br = len(matrix) - 1 
        
        while tl <= br and bl <= tr:
            for i in range(bl,  tr + 1):
                element.append(matrix[tl][i])
            tl += 1

            for i in range(tl, br + 1):
                element.append(matrix[i][tr])
            tr -= 1

            if tl <= br:
                for i in range(tr, bl -1, -1):
                    element.append(matrix[br][i])
                br -= 1

            if bl <= tr:
                for i in range(br, tl - 1, -1):
                    element.append(matrix[i][bl])
                bl += 1 

        return element

            

matrix = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7], [14,23,22,21,8], [13,12,11,10,9]]

print(Solution().spiralOrder(matrix))