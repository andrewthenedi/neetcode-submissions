class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # T: O(LOG(M * N)) | S: O(1)
        # M = Number of rows
        # N = Number of cols
        row_lower, row_upper = 0, len(matrix) - 1
        col_lower, col_upper = 0, len(matrix[0]) - 1
        while row_lower <= row_upper and col_lower <= col_upper:
            row_mid = row_lower + (row_upper - row_lower) // 2
            col_mid = col_lower + (col_upper - col_lower) // 2
            curr = matrix[row_mid][col_mid]
            if curr == target:
                return True
            elif curr < target:
                if target <= matrix[row_mid][col_upper]:
                    col_lower = col_mid + 1
                else:
                    row_lower = row_mid + 1
            else:
                if target >= matrix[row_mid][col_lower]:
                    col_upper = col_mid - 1
                else:
                    row_upper = row_mid - 1
        return False
