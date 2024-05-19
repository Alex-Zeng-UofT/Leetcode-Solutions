class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for i in range(len(s)):

            if s[i] != ']':
                stack.append(s[i])
            
            else:
                substr = ""

                while stack[-1] != '[':
                    substr = stack.pop() + substr
                
                stack.pop()

                num =""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * substr)

        return "".join(stack)