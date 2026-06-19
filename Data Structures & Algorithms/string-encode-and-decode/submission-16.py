class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for str in strs:
            result += f"{len(str)}#{str}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = s.find('#',i)

            length = int(s[i:j])

            i = j + 1

            result.append(s[i: i + length])

            i += length

        return result
