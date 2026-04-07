# Brute Force

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        # column
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board [i][col] in seen:
                    return False
                seen.add(board[i][col])

        # Square
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        return True


