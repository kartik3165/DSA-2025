# # matrix = [[0,1,2,0], Output: [[0,0,0,0],
# #           [3,4,5,2],          [0,4,5,0],
# #          [1,3,1,5]]          [0,3,1,0]]


class BrutForce(object):

    def setRowZero(self, mat, row):
        m = len(mat)
        for i in range(m):
            mat[row][i] = -1

    def setColZero(self, mat, col):
        n = len(mat[0]) 
        for i in range(n):
            mat[i][col] = -1

    def setZeroes(self, mat):
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    mat[i][j] = -1
                    self.setRowZero(mat, i)
                    self.setColZero(mat, j)
        
        for k in range(m):
            for l in range(n):
                if mat[k][l] == -1:
                    mat[k][l] = 0
        return mat

class betterSol(object):

    def findZero(self, mat):
        m = len(mat)
        n = len(mat[0])
        rowBar, colBar = [1] * m, [1] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    rowBar[i] = 0
                    colBar[j] = 0

        for k in range(m):
            for m in range(n):
                if rowBar[k] == 0 or colBar[m] == 0:
                    mat[k][m] = 0
        
        return mat
    
def printMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            print(f'{i},{j} = {mat[i][j]}')

mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

printMatrix(betterSol().findZero(mat))






            

