class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            # Coordinate Mapping Logic:
            # We treat the 2D matrix as a virtual 1D array.
            # To get the row: divide the index by the number of elements in each row (n).
            # To get the col: get the remainder of the index divided by n.
            middle = (l + r) // 2
            row, col = middle // n, middle % n
            print(middle, row, col)
            if target > matrix[row][col]:
                l = middle + 1
            elif target < matrix[row][col]:
                r = middle - 1
            else: 
                return True
        return False
                