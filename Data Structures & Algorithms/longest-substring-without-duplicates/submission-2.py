# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub_s = set()
        longest = 0
        for r in range(len(s)):
            # If we see a repeating character, 
            # shrink the window from the left until the duplicate is gone.
            while s[r] in sub_s:
                sub_s.remove(s[l])
                l += 1
            # Add the current character to our window
            sub_s.add(s[r])
            # Find the window size
            if len(sub_s) > longest:
                longest = len(sub_s)
        return longest
            
