class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isoperand(val):
            if val == '+' or val == "-" or val == "/" or val == "*":
                return True
            else:
                return False
        def compute(val1,val2,token):
            if token == "+":
                return int(val1 + val2)
            elif token == "-":
                return int(val1 - val2)
            elif token == "*":
                return int(val1 * val2)
            elif token == "/":
                return int(val1/val2)
            else:
                print(f"Error parsing {val1} {token} {val2}")
                return 0
                
        if len(tokens) == 0:
            return None
        stack = [] # declare list to be used as stack 
        for token in tokens: # iterate through items in tokens
            if isoperand(token):
                #pop two elements, apply operand and push
                val2 = stack.pop()
                val1 = stack.pop()
                answ = compute(val1,val2,token)
                stack.append(answ)
            else:
                stack.append(int(token))
        return stack[0]

        