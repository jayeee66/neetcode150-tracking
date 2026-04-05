class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for str in strs:
            s_str = ''.join(sorted(str))
            m[s_str].append(str)
        return list(m.values())




