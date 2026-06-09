class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len, cur_len = 1,1
        nums.sort()
        tocheck = nums[0]

        for i in range(1,len(nums)):
            if (nums[i] != tocheck) and (nums[i] - tocheck == 1):
                cur_len += 1
                if max_len < cur_len:
                    max_len = cur_len
                tocheck = nums[i]
            elif (nums[i] != tocheck) and (nums[i] - tocheck != 1):
                cur_len = 1
                tocheck = nums[i]
        return max_len