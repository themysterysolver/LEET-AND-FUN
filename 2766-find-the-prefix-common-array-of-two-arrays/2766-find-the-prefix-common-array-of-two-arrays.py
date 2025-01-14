class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hash=dict()
        result=[]
        for i in range(len(A)):
            #print(i)
            hash[A[i]]=hash.get(A[i],0)+1
            hash[B[i]]=hash.get(B[i],0)+1
            count=0
            if hash[A[i]]==2:
                count+=1
            if hash[B[i]]==2 and A[i]!=B[i]:
                count+=1
            if i==0:
                result.append(count)
            else:
                #print('chckpt1',result[-1],result)
                result.append(count+result[-1])
        return result
