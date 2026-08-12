class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answ = []
        candidates = sorted(candidates)
        def rec(total,path,start,candidates,last):
            if total == target:
                #print(f"found answer")
                answ.append(path.copy())
                return
            for i in range(start,len(candidates)):
                num = candidates[i]
                if num=='#' or total+num > target or (i > 0 and candidates[i] == candidates[i - 1]):
                    continue
                path.append(num)
                candidates[i] = '#'
                #print(f"candidates = {candidates} num ={num} total = {total+num} last = {last}")
                rec(total+num,path,i+1,candidates,num)
                candidates[i] = num
                path.pop()
        rec(0,[],0,candidates,-1)
        return answ