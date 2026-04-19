class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_set_group = list()
        box_set_group = list()

        for i in range(len(board)):
            row_set = set()

            for j in range(len(board[i])):
                if board[i][j] != "." and board[i][j] in row_set:
                    print(f"row check failure: {board[i][j]}")
                    return False

                row_set.add(board[i][j])

                if j < len(column_set_group):
                    if board[i][j] != "." and board[i][j] in column_set_group[j]:
                        print(f"column check failure: {board[i][j]}")
                        return False
                    
                    column_set_group[j].add(board[i][j])
                elif j == len(column_set_group):
                    column_set_group.append(set(board[i][j]))
                else:
                    print("what the heck")

                square_idx = (int(i/3))*3 + int(j/3)

                if square_idx < len(box_set_group):
                    if board[i][j] != "." and board[i][j] in box_set_group[square_idx]:
                        print(f"square check failure at square_idx={square_idx} and (i,j)={(i,j)}: {board[i][j]}")
                        return False
                    
                    box_set_group[square_idx].add(board[i][j])
                elif square_idx == len(box_set_group):
                    box_set_group.append(set(board[i][j]))
                else:
                    print("what the heck")
        
        return True

