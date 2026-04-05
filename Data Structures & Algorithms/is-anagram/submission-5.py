class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m_s = defaultdict(int)
        m_t = defaultdict(int)
        for i in range(len(s)):
            m_s[s[i]] += 1
            m_t[t[i]] += 1
        return m_s == m_t
            
