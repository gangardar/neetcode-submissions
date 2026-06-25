class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        max_seq = 0
        l = 0

        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            max_seq = max(max_seq, len(myset))        
        return max_seq


        