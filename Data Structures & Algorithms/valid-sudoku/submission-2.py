class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for idx_row in range(len(board)):
            for idx_col in range(len(board)):
                digit = board[idx_row][idx_col]
                if digit != ".":
                    digit = int(digit)
                    keys = (("row", idx_row, digit), ("col", idx_col, digit), ("box", ((idx_row//3)*3 + idx_col//3), digit))
                    for key in keys:
                        if key in seen:
                            print(key)
                            print(keys, seen)
                            return False
                        seen.add(key)
        return True