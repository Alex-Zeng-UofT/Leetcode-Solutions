class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        self.total = 1
        self.zero = 0

    def add(self, num: int) -> None:

        self.nums.append(max(1, num) * self.total)

        if num > 0:
            self.total *= num
        else:
            self.zero = len(self.nums) - 1
        

    def getProduct(self, k: int) -> int:

        return 0 if (len(self.nums) - k) <= self.zero else self.total // self.nums[-k - 1]

    

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)