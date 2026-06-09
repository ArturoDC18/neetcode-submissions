class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0
        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while (num+length) in numSet:
                    length += 1
                max_len = max(length, max_len)
        return max_len 