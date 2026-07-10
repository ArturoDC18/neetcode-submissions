class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums = sorted(nums1)
        print(nums)
        if len(nums) == 1:
            return float(nums[0])
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[(len(nums)//2)-1])/2
        else:
            print(f'returning index [{(len(nums)//2)}]')
            return float(nums[(len(nums)//2)])