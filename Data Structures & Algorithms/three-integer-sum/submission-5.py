class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p1, p3 = 0,(len(nums)-1)
        solution = defaultdict(list)
        for p1 in range(len(nums)-1):
            p2 = p1 + 1
            while p2 < p3:
                suma = nums[p1] + nums[p2] + nums[p3]
                if suma == 0:
                    solution[(nums[p1],nums[p2],nums[p3])]=[nums[p1],nums[p2],nums[p3]] 
                    p2 += 1
                elif suma < 0:
                    p2 += 1
                else:
                    p3 -= 1
            p3 = len(nums)-1
        
        return list(solution.values())