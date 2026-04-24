class Solution:
    # we can go through the grid recursively and cache values as we iterate
    # we want to know from each square, how many unique paths are there to
    # get to the target
    def uniquePaths(self, m: int, n: int) -> int:
        # the bottom row is going to be filled with all 1s since moving right is the only new square
        # you can have. previous rows will already be calculated so there's no need to calculate going
        # up
        row = [1] * n

        # for all rows
        for i in range(m - 1):
            new_row = [1] * n # base row case
            
            # for all cols going backwards since last col is all 1s
            for j in range(n - 2, -1, -1):
                # each cell val will be equal to the cell val to the right + the orig cell value in row
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        
        return row[0] # this is unique path count from the starting square at the top left

        