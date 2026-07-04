class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answ= []
        for r in range(k,len(nums)+1):
            answ.append(max(set(nums[r-k:r])))
        return answ
    