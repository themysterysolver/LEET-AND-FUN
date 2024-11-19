class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result=[]
        if k==result:
            return code
        for i in range(len(code)):
            sumi=0
            if k>0:
                for j in range(i+1,i+1+k):
                    sumi+=code[j%len(code)]
            if k<0:
                for j in range(i-abs(k),i):
                    print(i,j)
                    sumi+=code[(j+len(code))%len(code)]
                print('----------------------')
            result.append(sumi)
        return result