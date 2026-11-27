class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_col = set()
        set_row = set()

        for idx_row in range(len(board)):
            set_row_c = set()
            for idx_col in range(len(board)):
                val_c = board[idx_row][idx_col]
                if val_c != ".":
                    if val_c in set_row_c:
                        return False
                    else:
                        set_row_c.add(val_c)

        for idx_col in range(len(board)):
            set_col_c = set()
            for idx_row in range(len(board)):
                val_c = board[idx_row][idx_col]
                if val_c != ".":
                    if val_c in set_col_c:
                        return False
                    else:
                        set_col_c.add(val_c)
        
        for idx_row_block in range(0, len(board), 3):
            for idx_col_block in range(0, len(board), 3):
                set_c = set()
                for idx_row in range(idx_row_block, idx_row_block+3):
                    for idx_col in range(idx_col_block, idx_col_block+3):
                        val_c = board[idx_row][idx_col]
                        if val_c != ".":
                            if val_c in set_c:
                                return False
                            else:
                                set_c.add(val_c)
        return True