class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        minutes = 0
        fresh_oranges = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        while queue and fresh_oranges > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = dr + row, dc + col

                    if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1):
                        continue
                    
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh_oranges -= 1
            minutes += 1
        
        return minutes if fresh_oranges == 0 else -1

                
