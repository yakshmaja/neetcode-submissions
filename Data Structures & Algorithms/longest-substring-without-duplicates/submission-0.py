class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i = 0
        maxWS = 0
        for j in range(len(s)):
            if s[j] in map and map[s[j]] >= i:
                i = map[s[j]] + 1
            map[s[j]] = j
            currWS = j-i+1
            maxWS = max(currWS,maxWS)
        return maxWS