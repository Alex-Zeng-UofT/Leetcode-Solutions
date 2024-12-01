class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        missings = set()

        for num in arr:

            if num in missings:
                return True

            missings.add(num * 2)
            
            if num % 2 == 0:
                missings.add(num // 2)
        
        return False