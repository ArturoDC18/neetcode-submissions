class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(p1,p2):
            return (p2-p1) * min(heights[p1], heights[p2])
        maxH, p1, p2 = 0, 0, len(heights)-1
        while p1 != p2:
            area = getArea(p1,p2)
            if area > maxH:
                maxH = area
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxH