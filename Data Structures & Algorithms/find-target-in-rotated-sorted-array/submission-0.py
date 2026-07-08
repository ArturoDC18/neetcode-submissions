class Solution:
    def findR(self, nums):
            if nums[-1]>=nums[0]:
                return 0
            l,r = 0, len(nums)-1
            while True:
                c=(r+l)//2
                if nums[c+1]<nums[c]:
                    return (c+1)
                elif nums[r]<nums[l]:
                    l = c
                else:
                    r = c-1
    def search(self, nums: List[int], target: int) -> int:
        R = self.findR(nums)
        l, r = R, (len(nums)-1)+R
        while l<=r:
            c = ((l+r) //2)
            if nums[c%len(nums)] == target:
                return c%len(nums)
            elif nums[c%len(nums)] < target:
                l = c+1
            else:
                r = c-1
        return -1