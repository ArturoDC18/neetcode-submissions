class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(l,r,nums,target):
            if l>r:
                return -1
            c = l + (r-l) // 2
            if nums[c] == target:
                return c
            elif nums[c] < target:
                return bsearch(c+1, r, nums, target)
            else:
                return bsearch(l, c-1, nums, target)
        return bsearch(0,len(nums)-1, nums, target)
