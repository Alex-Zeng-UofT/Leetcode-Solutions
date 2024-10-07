class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []

        for letter in s:
            
            if not stack: 
                stack.append(letter)
            elif stack[-1] == 'A' and letter == 'B':
                stack.pop()
            elif stack[-1] == 'C' and letter == 'D':
                stack.pop()
            else:
                stack.append(letter)

        return len(stack)