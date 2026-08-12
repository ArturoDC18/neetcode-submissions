class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answ = []
        candidates = sorted(candidates)
        def rec(total,path,start):
            if total == target:
                answ.append(path.copy())
                return
            for i in range(start,len(candidates)):
                num = candidates[i]
                if (i > start and candidates[i] == candidates[i - 1]):
                    continue
                if total + num > target:
                    break
                path.append(num)
                rec(total+num,path,i+1)
                path.pop()
        rec(0,[],0)
        return answ