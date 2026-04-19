class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops_stack = []

        for val in tokens:
            if val == "+":
                ops_stack.append(ops_stack.pop() + ops_stack.pop())
            elif val == "-":
                second_val = ops_stack.pop()
                first_val = ops_stack.pop()
                ops_stack.append(first_val - second_val)
            elif val == "*":
                ops_stack.append(ops_stack.pop() * ops_stack.pop())
            elif val == "/":
                second_val = ops_stack.pop()
                first_val = ops_stack.pop()
                ops_stack.append(int(first_val / second_val))
            else:
                ops_stack.append(int(val))
        
        return ops_stack[-1]

        