class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item in "({[":
                stack.append(item)
            elif item in ")}]":
                if not stack:
                    return False
                elem = stack.pop()
                if elem == '(' and item == ')':
                    continue
                elif elem == '{' and item == '}':
                    continue
                elif elem == '[' and item == ']':
                    continue
                else:
                    return False
            print(f"Processed {item}")
        
        if not stack:
            return True
        return False