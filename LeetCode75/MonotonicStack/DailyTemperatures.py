class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ret = []

        for i in range(len(temperatures)):
            ret.append(0)
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ret[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return ret