class Solution:
    def maxOperations(self, s: str) -> int:
        arr=[]
        i=0
        while i<len(s):
            if s[i]=="1":
                arr.append(s[i])
            else:
                arr.append(s[i])
                while i+1<len(s) and s[i]==s[i+1]:
                    i+=1
            i+=1
        print(arr)
        count=0
        zeros=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]=='0':
                zeros+=1
            else:
                count+=zeros
            #print(i,zeros,count)
        return count