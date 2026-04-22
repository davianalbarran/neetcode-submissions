class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def bfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r, c) in visited or grid[r][c] == -1):
                return
            
            visited.add((r, c))
            queue.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        dist = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = dist

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            dist += 1


        