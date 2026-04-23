# it's time to get greedy... Dijkstra's!
class Solution:
    # we're starting from grid[0][0]
    # we're targeting grid[len(grid) - 1][len(grid[0]) - 1]
    # we want to find the path to our goal with the SMALLEST max height
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        min_heap = [(grid[0][0], 0, 0)] # cost, row coord, col coord
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_height = 0

        while min_heap:
            cost, r, c = heapq.heappop(min_heap)
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS -1:
                return cost # this is guaranteed to be hit at some point since we are traversing the whole array
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc

                if (neiR < 0 or neiC < 0 or
                    neiR == ROWS or neiC == COLS or
                    (neiR, neiC) in visited):
                    continue
                
                visited.add((neiR, neiC))
                heapq.heappush(min_heap, (max(cost, grid[neiR][neiC]), neiR, neiC)) # ensure we keep the max cost