# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            current = intervals[i]
            last = ans[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                ans.append(intervals[i])

        return ans
            
        
intervals = [[1,3],[2,6],[8,10],[15,18]]

# Output: [[1,6],[8,10],[15,18]]
    
print(Solution().merge(intervals))
        

