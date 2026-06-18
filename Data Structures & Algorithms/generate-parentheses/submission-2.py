#backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(l, r):
            if l == r == n:
                res.append("".join(stack))
                return
            if l < n:
                stack.append("(")
                dfs(l+1, r)
                stack.pop()
            # count ')' SHOULDN'T exceed count '('
            if r < l:
                stack.append(")")
                dfs(l, r+1)
                stack.pop()
        dfs(0 ,0)
        return res

            