class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2: return None
        x = 0
        while x < len(nums):
            y = x +1
            while y < len(nums):
                if nums[x] + nums[y] == target:
                    return [x,y]
                else:
                    y = y+1
            x = x+1

        