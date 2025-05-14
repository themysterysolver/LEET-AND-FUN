#created new arrays else it erases the next value genius!
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD=10**9+7
        arr=[0]*26
        for c in s:
            arr[ord(c)-ord('a')]+=1
        #print([i for i in range(len(arr))])
        print(arr)
        for T in range(t):
            newArr=[0]*26
            for i in range(26):
                if i==25:
                    newArr[0]+=arr[i]
                    newArr[1]+=arr[i]
                else:
                    newArr[i+1]=arr[i]
                #print('i:',i,arr)
            #print(T,newArr)
            arr=newArr
        return sum(arr)%MOD
