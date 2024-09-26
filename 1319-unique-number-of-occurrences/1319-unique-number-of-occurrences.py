class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict()
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        a=d.values()
        print(a)
        if len(a)!=len(set(a)):
            return False
        return True
