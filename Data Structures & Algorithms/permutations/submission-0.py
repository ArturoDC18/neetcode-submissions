class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answ = []
        def rec(path):
            if len(path) >= len(nums):
                answ.append(path.copy())
                return
            for i in range(len(nums)):
                num = nums[i]
                if num == '#':
                    continue
                path.append(num)
                nums[i]='#'
                rec(path)
                nums[i]=num
                path.pop()
        rec([])
        return answ