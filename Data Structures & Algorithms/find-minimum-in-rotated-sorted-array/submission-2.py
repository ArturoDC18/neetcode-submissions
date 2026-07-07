class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        while True:
            c = (r+l)//2
            if nums[c+1] < nums[c]:
                return nums[c+1]
            elif nums[r] < nums[l]:
                l = c
            else:
                r = c-1

        