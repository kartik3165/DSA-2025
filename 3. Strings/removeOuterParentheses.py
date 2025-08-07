# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# Example 2:
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

# Example 3:
# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".



class Solution(object):
    def removeOuterParentheses(self, s):
        left = 0
        right = 0
        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1
        print(left)
        print(right)

Solution().removeOuterParentheses(s='((())')