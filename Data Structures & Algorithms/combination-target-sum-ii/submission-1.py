class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        candidates.sort()

        def dfs(start, curr):
            if curr == target:
                res.append(subset.copy())
                return
            
            if curr > target:
                return
            #try each 
            for i in range(start, len(candidates)):
                # Ingnore the same element, prevent duplicated subsets
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(i + 1, curr + candidates[i])
                subset.pop()
        dfs(0, 0)
        return res