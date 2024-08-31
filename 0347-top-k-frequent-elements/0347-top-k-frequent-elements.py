class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        l=list(set(nums))
        a=[]
        for i in l:
            d[i]=nums.count(i)
        print (d)
        di=[[val,key] for key,val in d.items()]
        print (di)
        di=sorted(di,key=lambda x:x[0],reverse=True)
        print (di)
        while k!=0:
            a.append(di[k-1][-1])
            k=k-1
        return a
            