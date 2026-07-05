class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS -1
        while top <= bot:
            row = (top + bot) //2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, len(matrix[row])-1
        while l <= r:
            c = (l+r) //2
            if matrix[row][c] == target:
                return True 
            elif matrix[row][c] < target:
                l = c+1
            else:
                r = c-1
        return False
        
