class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash=dict()
        for i in edges:
            for j in i:
                if j not in hash:
                    hash[j]=1
                else:
                    hash[j]+=1
        print(hash)
        max_val=max(hash.values())
        print(max_val)
        for key,val in hash.items():
            if val==max_val:
                return key
        