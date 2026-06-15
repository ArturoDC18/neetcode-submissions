class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, maxim = 0,1,0
        if len(height) <= 2:
            return 0
        maxr = -1
        def compute(l,r):
            num = 0
            for val in range(l +1,r):
                num += min(height[l], height[r]) - height[val]
            return num
        while l < len(height) -1:
            if r == len(height) and maxr == -1:
                return maxim
            elif r == len(height) and maxr != -1:
                maxim += compute(l,maxr)
                l = maxr
                r = maxr 
                maxr = -1
            elif height[r] >= height[l]:
                maxim += compute(l,r)
                l = r
                maxr = -1
            elif height[l] != 0 and height[r] < height[l]:
                if maxr == -1 or height[r] > height[maxr]:
                    maxr = r
            r += 1
        return maxim