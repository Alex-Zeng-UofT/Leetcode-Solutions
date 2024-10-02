class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        temp = sorted(set(arr))

        map = {val : i + 1 for i, val in enumerate(temp)}

        return [map[val] for val in arr]
        