class Solution:
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}
        def detbox(column,row) -> int:
            if column < 3:
                if row < 3:
                    return 1
                elif row < 6:
                    return 2
                else:
                    return 3
            elif column < 6: 
                if row < 3:
                    return 4
                elif row < 6:
                    return 5
                else:
                    return 6
            else:
                if row < 3:
                    return 7
                elif row < 6:
                    return 8
                else:
                    return 9
        def compute(num, hashh) -> bool:
            if hashh not in dic:
                dic[hashh] = set(num)
                return True
            elif num in dic[hashh]:
                return False
            else:
                dic[hashh].add(num)
                return True
        for column in range(len(board)):
            for row in range(len(board)):
                num = board[column][row]
                if num != ".":
                    if not compute(num, 'c'+str(column)) or not compute(num, 'r'+str(row)) or not compute(num, 'b'+str(detbox(column,row))):
                        return False       
        return True