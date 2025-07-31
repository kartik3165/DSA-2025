class Solution(object):
    def generateRow(self, row):
        ans = 1
        ans_list = [1]  
        for col in range(1, row + 1):
            ans = ans * (row - col + 1)
            ans = ans // col
            ans_list.append(ans)
        return ans_list

    def generate(self, numRows):
        tri = []
        for i in range(numRows):
            tri.append(self.generateRow(i))
        return tri

print(Solution().generate(5))
