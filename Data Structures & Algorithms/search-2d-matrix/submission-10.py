class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for lista in matrix:
            nums += lista
        def binsearch(l,r,nums,target):
            if l > r:
                return False
            c = l + (r-l) //2
            print(f"{l}, {c}, {r}")
            if nums[c] == target:
                return True
            elif nums[c] > target:
                return binsearch(l, c-1,nums, target)
            else:
                return binsearch(c+1, r, nums, target)
        return binsearch(0,len(nums)-1, nums, target)