class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub_s = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in sub_s:
                sub_s.remove(s[l])
                l += 1
            sub_s.add(s[r])
            if len(sub_s) > longest:
                longest = len(sub_s)
        return longest
            