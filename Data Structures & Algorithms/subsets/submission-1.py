class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):

                res.append(subset.copy())
                return
            # don't pick numbers
            dfs(i + 1)
            # pick nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
        dfs(0)
        return res



            
                
