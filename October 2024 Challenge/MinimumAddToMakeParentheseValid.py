class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        count = 0

        for bracket in s:
            if bracket == '(':
                stack.append(bracket)
            elif not stack:
                count += 1
            else:
                stack.pop()

        return count + len(stack)