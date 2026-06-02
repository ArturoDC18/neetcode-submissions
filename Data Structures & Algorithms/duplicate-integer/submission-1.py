class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        checker = False
        for item in nums:
            if item in hashset:
                return True
            hashset[item] = item
        return False

        