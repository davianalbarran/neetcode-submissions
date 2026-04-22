class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r_mod, c_mod = row + dr, col + dc
                    if (r_mod in range(ROWS) and
                        c_mod in range(COLS) and
                        grid[r_mod][c_mod] == "1" and
                        (r_mod, c_mod) not in visited):
                        queue.append((r_mod, c_mod))
                        visited.add((r_mod, c_mod))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands