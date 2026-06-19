class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: "length#string"
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter '#'
            j = s.find('#', i)
            
            # The length of the string is the part before '#'
            length = int(s[i:j])
            
            # Move index to the start of the actual string
            i = j + 1
            
            # Extract the string based on the length
            res.append(s[i : i + length])
            
            # Move the pointer forward by the string's length
            i += length
            
        return res