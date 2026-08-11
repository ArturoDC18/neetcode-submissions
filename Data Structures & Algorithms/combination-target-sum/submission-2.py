class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answ = []
        def rec(total,path,start):
            if total == target:
                answ.append(path.copy())
                return
            for i in range(start,len(nums)):
                num = nums[i]
                if total+num > target:
                    continue
                path.append(num)
                rec(total+num,path,i)
                path.pop()
        rec(0,[],0)
        return answ
        