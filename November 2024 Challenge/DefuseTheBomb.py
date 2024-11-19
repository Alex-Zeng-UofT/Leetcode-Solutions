class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)

        if k == 0: return [0] * n

        ret = []
        
        is_positive = k > 0

        if not is_positive:
            code.reverse()
            k *= -1

        cur_sum = code[0]
        code.extend(code[:k + 1].copy())

        for i in range(1, k + 1):
            cur_sum += code[i]
        
        for i in range(n):
            cur_sum -= code[i]
            ret.append(cur_sum)
            cur_sum += code[i + k + 1]

        return ret if is_positive else ret[::-1]
        