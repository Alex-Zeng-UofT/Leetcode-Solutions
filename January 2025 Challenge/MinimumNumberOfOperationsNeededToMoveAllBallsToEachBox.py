class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        forwards, backwards = [0] * n, [0] * n

        moves, count = 0, 0
        for i in range(n - 1):
            
            moves += count

            if boxes[i] == '1':
                moves += 1
                count += 1

            forwards[i + 1] = moves

        moves, count = 0, 0
        for i in range(n - 1, 0, -1):

            moves += count

            if boxes[i] == '1':
                moves += 1
                count += 1

            backwards[i - 1] = moves

        return [forwards[i] + backwards[i] for i in range(n)]