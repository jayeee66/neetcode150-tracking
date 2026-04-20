class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                # Plus and multiplication doesn't matter the order,
                # so don't need to consider it.
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # b in the bottom, so need to indentify the order
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
                print(stack)
        return stack[0]