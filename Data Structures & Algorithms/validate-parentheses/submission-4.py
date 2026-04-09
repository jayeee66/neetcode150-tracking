class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {'(':')', '{':'}', '[':']'}
        for p in s:
            if p not in par:
                if stack and par[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        # print(stack)
        return len(stack) == 0