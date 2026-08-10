class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answ = [[]]
        for number in nums:
            for item in answ.copy():
                copy = item.copy()
                copy.append(number)
                answ.append(copy)
        return answ
