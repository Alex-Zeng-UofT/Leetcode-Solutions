class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and self.pings[0] < t - 3000:
            self.pings.pop(0)

        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)