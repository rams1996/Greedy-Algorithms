class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        ptrG=0
        for i in range(len(s)):
            if ptrG>=len(g):
                break
            if s[i]>=g[ptrG]:
                ptrG+=1
        return ptrG
        
        
        
        
        
        
        
