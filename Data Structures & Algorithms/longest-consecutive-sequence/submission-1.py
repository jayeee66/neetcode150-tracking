# Hash set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set to store numbers
        num_set = set(nums)
        # longest streak default 0
        longest = 0
        for num in num_set:
            # Find the beginning number and keep changing
            if num - 1 not in num_set:
                curr = num
                # print(first)
                leng = 1
                while (curr + 1) in num_set:
                    curr += 1
                    leng += 1
                if leng > longest:
                    longest = leng

        return longest
