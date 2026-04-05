class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list) 
        

        for str in strs:
            count = [0] * 26
            for char in str:
                index = ord(char) - ord('a')
                count[index] += 1
            m[tuple(count)].append(str)
        return list(m.values())
        







