class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxf = maxb = 0
        area = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= maxf:
                    maxf = height[l]
                else:
                    area += maxf - height[l]
                l += 1
            else:
                if height[r] >= maxb:
                    maxb = height[r]
                else:
                    area += maxb - height[r]
                r -= 1

        return area