class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        class StackNode:
            def __init__(self, temp, pos):
                self.temp = temp
                self.pos = pos
        
        answ = [0] * len(temperatures)
        stack = []
        pos = 0
        for temp in temperatures:
            if len(stack) != 0:
                while stack and stack[-1].temp < temp:
                    answ[stack[-1].pos] = pos - stack[-1].pos 
                    stack.pop()
            stack.append(StackNode(temp, pos))
            pos += 1
        return answ