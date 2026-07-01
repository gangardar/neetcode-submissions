class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        res = 0

        for ch in s:
            while ch in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(ch)
            res = max(res, len(mySet))
        return res
        
            