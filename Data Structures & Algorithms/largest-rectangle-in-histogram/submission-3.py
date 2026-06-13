class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                height, pos = stack.pop()
                A = height * (i-pos)
                if A > largest:
                    largest = A
                start = pos
            stack.append((heights[i], start))

        while stack:
            height, pos = stack.pop()
            A = height * (len(heights) - pos)
            if A > largest:
                largest = A

        return largest