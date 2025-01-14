class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA=set()
        setB=set()
        result=[]
        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            result.append(len(setA & setB))
        return result
