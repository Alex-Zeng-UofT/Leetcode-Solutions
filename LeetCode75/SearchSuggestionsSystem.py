class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        cur = sorted(products)
        next, ret = [], []
        
        for i in range(len(searchWord)):

            for product in cur:
                if len(product) > i and searchWord[i] == product[i]:
                    next.append(product)

            cur = next.copy()
            ret.append(cur[:min(len(cur), 3)].copy())
            next = []

        return ret