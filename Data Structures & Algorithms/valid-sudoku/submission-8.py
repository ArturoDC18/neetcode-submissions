class Solution:
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = defaultdict(set)
        def compute(num, hashh) -> bool:
            if hashh in dic and num in dic[hashh]:
                return False
            else:
                dic[hashh].add(num)
                return True
        for column in range(len(board)):
            for row in range(len(board)):
                num = board[column][row]
                if num != ".":
                    if (not compute(num, 'c'+str(column)) 
                    or not compute(num, 'r'+str(row)) 
                    or not compute(num, 'b'+str(column//3)+str(row//3))):
                        return False       
        return True