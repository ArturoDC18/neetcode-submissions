class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answ, maxi = [], max(set(nums[:k]))
        answ.append(maxi)
        for r in range(k+1,len(nums)+1):
            if maxi == nums[r-k-1] or nums[r-1] > maxi:
                maxi = max(set(nums[r-k:r]))
            answ.append(maxi)
        return answ