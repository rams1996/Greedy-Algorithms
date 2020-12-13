class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        if not A:
            return A
        from collections import defaultdict
        oldAdict=defaultdict(list)
        oldBdict=defaultdict(list)
        for i in range(len(A)):
            oldAdict[A[i]].append(i)
            oldBdict[B[i]].append(i)
        oldA=A.copy()
        oldB=B.copy()
        A.sort()
        B.sort()
        Aindex=0
        Bindex=0
        count=0
        result=[]
        notused=[]
        while(Aindex<len(A)):
            if A[Aindex]>B[Bindex]:
                result.append(A[Aindex])
                Aindex+=1
                Bindex+=1
            else:
                notused.append(A[Aindex])
                Aindex+=1
                
                
        res=[0]*len(B)
        finalptr=0
        newfinalptr=0
        for i in B:
            if finalptr<len(result):
                res[oldBdict[i][-1]]=result[finalptr]
                oldBdict[i].pop()
                finalptr+=1
            else:
                res[oldBdict[i][-1]]=notused[newfinalptr]
                oldBdict[i].pop()
                newfinalptr+=1
        return res
                
            
        
