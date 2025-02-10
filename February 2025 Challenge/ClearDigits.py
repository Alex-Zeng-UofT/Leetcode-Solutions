class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for letter in s:
            if letter.isdigit():
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)