class MedianFinder:
    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        heapq.heapify(self.small_heap)
        heapq.heapify(self.large_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)
        if (self.small_heap and self.large_heap and (-1 * self.small_heap[0]) > self.large_heap[0]):
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        
        if len(self.large_heap) > len(self.small_heap) + 1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return float(-self.small_heap[0])
        if len(self.large_heap) > len(self.small_heap):
            return float(self.large_heap[0])
        
        return ((-1 * self.small_heap[0]) + self.large_heap[0])/2.0