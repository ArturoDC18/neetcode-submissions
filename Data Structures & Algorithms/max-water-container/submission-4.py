class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(p1,p2):
            tall = min(heights[p1],heights[p2])
            return (p2-p1) * tall
        maxH = 0
        for i, height in enumerate(heights):
            for seen in range(0,i):
                area = getArea(seen,i)
                if area > maxH:
                    maxH = area
        
        return maxH