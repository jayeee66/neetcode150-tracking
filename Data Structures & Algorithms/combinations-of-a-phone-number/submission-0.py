class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subset = []
        digitToChar = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        def dfs(i):
            if i == len(digits):
                res.append(''.join(subset))
                return
            for char in digitToChar[digits[i]]:
                # add char
                subset.append(char)
                # find next
                dfs(i + 1)
                subset.pop()
        if digits:
            dfs(0)
        return res
            


