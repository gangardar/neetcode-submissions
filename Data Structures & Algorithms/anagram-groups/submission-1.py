class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            result.setdefault(sorted_str, []).append(str)
        
        return list(result.values())
