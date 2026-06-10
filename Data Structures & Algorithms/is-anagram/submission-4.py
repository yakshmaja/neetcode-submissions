class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s) != len(t):
            return False
        freqS , freqT = {} , {}
        for i in range(len(s)):
            freqS[s[i]] = freqS.get(s[i],0)+1
            freqT[t[i]] = freqT.get(t[i],0)+1
        return freqS == freqT"""

        """if len(s) != len(t):
            return False
        chars = {}
        for ch in s:
            chars[ch] = chars.get(ch , 0) + 1

        for ch in t:
            if ch not in chars:
                return False
            else:
                if chars[ch] == 0:
                    return False
                chars[ch] -= 1
        return True"""

        if len(s) != len(t):
            return False
        sort_s = sorted(s)
        sort_t = sorted(t)
        if sort_s == sort_t:
            return True
        return False



        