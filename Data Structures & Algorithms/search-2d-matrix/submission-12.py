class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bsearch(l,r,matrix, target,n):
            if l > r:
                return False
            c = l + (r-l) // 2
            row, col = c // n, c % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                return bsearch(c+1, r, matrix, target, n)
            else:
                return bsearch(l, c-1, matrix, target, n)
        return bsearch(0, len(matrix)*len(matrix[0])-1,matrix, target, len(matrix[0]))