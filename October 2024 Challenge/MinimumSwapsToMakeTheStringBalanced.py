class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unbalanced = 0

        for bracket in s:
            if bracket == '[':
                stack.append(bracket)
            elif stack:
                stack.pop()
            else:
                unbalanced += 1
        
        return (unbalanced + 1) // 2