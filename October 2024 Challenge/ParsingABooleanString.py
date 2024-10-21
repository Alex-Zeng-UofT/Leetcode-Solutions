class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def compute(operator: str, parameters: List[str]) -> str:

            if operator == '!':
                return "f" if parameters[0] == "t" else "t"

            if operator == '&':
                for boolean in parameters:
                    if boolean == 'f': return 'f'
                return 't'

            elif operator == '|':
                for boolean in parameters:
                    if boolean == 't': return 't'
                return 'f'

            return "lol"
        

        stack = []

        for char in expression:
            
            if char == ')':

                params = []
                while stack[-1] != '(':
                    params.append(stack.pop())

                stack.pop()
                operation = stack.pop()
                stack.append(compute(operation, params))
            
            elif char != ',':
                stack.append(char)

        return stack.pop() == 't'
     