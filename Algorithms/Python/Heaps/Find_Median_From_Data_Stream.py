# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        self.smallMax = []
        self.largeMin = []
        

    def addNum(self, num: int) -> None:
        heappush(self.smallMax, num*-1)
        if self.smallMax and self.largeMin and self.smallMax[0]*-1 > self.largeMin[0]:
            val = heappop(self.smallMax) * -1
            heappush(self.largeMin, val)
        
        if len(self.smallMax) - len(self.largeMin) > 1:
            val = heappop(self.smallMax) * -1
            heappush(self.largeMin, val)
        if len(self.largeMin) - len(self.smallMax) > 1:
            val = heappop(self.largeMin)
            heappush(self.smallMax, val * -1)

    def findMedian(self) -> float:
        if len(self.smallMax) > len(self.largeMin): return self.smallMax[0]*-1
        elif len(self.largeMin) > len(self.smallMax): return self.largeMin[0]
        else: return (self.largeMin[0] + self.smallMax[0]*-1) / 2
