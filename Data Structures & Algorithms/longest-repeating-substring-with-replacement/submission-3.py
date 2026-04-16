class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_freq = 0
        longest = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            # Update the max frequency found in the current window
            # This helps us identify the dominant character that we won't replace
            max_freq = max(max_freq, freq[s[r]])
            # (Window length - max_f) gives the number of characters we need to replace.
            # If this count exceeds k, the window is invalid.
            while r - l + 1 - max_freq > k:
                # Shrink the window from the left to keep the string continuous
                freq[s[l]] -= 1
                l += 1
                

            # Update the maximum length of a valid window found so far
            if r - l + 1 > longest:
                longest = r - l + 1

        return longest