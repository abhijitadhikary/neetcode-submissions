class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_set_row = [set() for _ in range(len(board))]
        list_set_col = [set() for _ in range(len(board))]
        list_set_block = [set() for _ in range(len(board))]

        for idx_row in range(len(board)):
            for idx_col in range(len(board)):
                val_c = board[idx_row][idx_col]
                if val_c != ".":
                    val_c = int(val_c)

                    if val_c not in list_set_row[idx_row]:
                        list_set_row[idx_row].add(val_c)
                    else:
                        return False
                    
                    if val_c not in list_set_col[idx_col]:
                        list_set_col[idx_col].add(val_c)
                    else:
                        return False
                    
                    if val_c not in list_set_block[(idx_row//3)*3 + idx_col//3]:
                        list_set_block[(idx_row//3)*3 + idx_col//3].add(val_c)
                    else:
                        return False
        return True