class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # T: O(N^2) | S: O(N^2)
        # N = Size of board
        visited_row = collections.defaultdict(set)
        visited_col = collections.defaultdict(set)
        visited_sqr = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                sqr = (row // 3, col // 3)
                if (
                    board[row][col] in visited_row[row] or
                    board[row][col] in visited_col[col] or
                    board[row][col] in visited_sqr[sqr]
                ):
                    return False
                visited_row[row].add(board[row][col])
                visited_col[col].add(board[row][col])
                visited_sqr[sqr].add(board[row][col])
        return True
