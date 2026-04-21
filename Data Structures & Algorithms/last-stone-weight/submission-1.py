class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [ -stone for stone in stones ]
        heapq.heapify(res)
        
        while len(res) > 1:
            first = heapq.heappop(res)
            second = heapq.heappop(res)
            if second > first:
                heapq.heappush(res, first - second)
        
        res.append(0)
        return abs(res[0])
            
