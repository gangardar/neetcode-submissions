class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for str in strs:
            res += f"{len(str)}#{str}"
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            i = j + 1

            result.append(s[i : i+length])
            
            i += length
        return result

