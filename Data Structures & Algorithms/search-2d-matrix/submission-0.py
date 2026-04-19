class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bot_row = 0, ROWS - 1

        while top_row <= bot_row:
            row = (top_row + bot_row) // 2

            if target > matrix[row][-1]:
                top_row = row + 1
            elif target < matrix[row][0]:
                bot_row = row - 1
            else:
                break
        
        if not (top_row <= bot_row):
            return False
        
        row = (top_row + bot_row) // 2

        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (r + l) // 2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
        