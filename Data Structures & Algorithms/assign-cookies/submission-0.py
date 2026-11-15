class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        children = len(g)
        cookie = len(s)
        i = 0 
        j = 0
        count = 0
        while i< children and j< cookie:
            if s[j] >= g[i]:
                count += 1
                i += 1
                j+= 1
            else:
                j+=1
        return count
        