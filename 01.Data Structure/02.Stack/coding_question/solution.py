class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        ans = []
        
        for char in S:
            if not stack:
                stack.append(char)
            elif len(stack) == 1:
                if char == '(':
                    ans.append(char)
                    stack.append(char)
                else:
                    stack.pop()
            else:
                if char == '(':
                    ans.append(char)
                    stack.append(char)
                else:
                    ans.append(char)
                    stack.pop()
        
        return ''.join(ans)
