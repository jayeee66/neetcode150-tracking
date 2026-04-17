class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        count = set()
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])  
                l += 1       
            count.add(s[r])
            if r - l + 1 > longest:
                longest = r - l + 1
            
        return longest
            