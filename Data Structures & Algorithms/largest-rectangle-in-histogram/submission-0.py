class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for he in heights:
            new_stack = [(1,he)]
            if he > largest:
                largest = he
            for longitud, height in stack:
                new_area = (longitud + 1) * min(height,he)
                if new_area > largest:
                    largest = new_area
                if min(height,he) != 0:
                    new_stack.append((longitud+1, min(height,he)))
            stack = new_stack
        return largest