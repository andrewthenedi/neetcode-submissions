class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # T: O(LOG(M * N)) | S: O(1)
        # M = Number of rows
        # N = Number of columns
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
