class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store index of daily temperature
        res = [0] * len(temperatures) # set a list store the difference
        for i, temp in enumerate(temperatures):
            # find the day that temperature higher than starting day
            while stack and temperatures[stack[-1]] < temp:
                # if find the top of index pop
                # then substract by the day to get the difference
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res