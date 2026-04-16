class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1_count = {}
        window_count = {}
        k = len(s1)
        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            window_count[s2[i]] = 1 + window_count.get(s2[i], 0)
        # print(s1_count, window_count)
        if s1_count == window_count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # Add new char 
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)
            # Remove old char
            window_count[s2[l]] -= 1
            # Remove the item, because it will stay in the hash map.
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]
            l += 1
            # print(s1_count, window_count)
            if window_count == s1_count:
                return True
        return False