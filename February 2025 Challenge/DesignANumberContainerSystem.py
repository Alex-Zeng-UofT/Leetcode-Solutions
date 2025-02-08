class NumberContainers:

    def __init__(self):
        self.container = {}
        self.idxs = {}        

    def change(self, index: int, number: int) -> None:
        
        self.container[index] = number

        if number not in self.idxs:
            self.idxs[number] = [index]
        else:
            heappush(self.idxs[number], index)


    def find(self, number: int) -> int:

        if number not in self.idxs or not self.idxs[number]:
            return -1

        while self.idxs[number] and self.container[self.idxs[number][0]] != number:
            heapq.heappop(self.idxs[number])

        return self.idxs[number][0] if self.idxs[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)