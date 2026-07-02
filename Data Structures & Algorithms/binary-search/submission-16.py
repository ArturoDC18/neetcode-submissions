class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0, len(nums)-1
        for _ in range(len(nums) +1//2):
            n = ((r-l) //2) + l
            print(l,n,r)
            if nums[n] == target:
                return n
            elif nums[n] > target:
                r = n -1
            else:
                l = n +1
        return -1
