class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i = 0
        maxws = 0
        for j in range(len(s)):
            if s[j] in map and map[s[j]]>=i:
                i = map[s[j]] + 1

            map[s[j]] = j
            currws = j-i+1
            maxws = max(currws,maxws)
        return maxws