class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxi=0
        arr=s.split(' ')
        maxi=max(len(a) for a in arr)
        print(arr,maxi)
        for i in range(len(arr)):
            arr[i]+=" "*(maxi-len(arr[i]))
        #print(arr)
        result=[]
        for i in range(len(arr[0])):
            r=""
            for j in range(len(arr)):
                r+=arr[j][i]
            result.append(r)
        for i in range(len(result)):
            result[i]=result[i].rstrip(' ')
        return result