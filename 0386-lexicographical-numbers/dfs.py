class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[]
        def dfs(cur):
            if cur>n:
                return
            ans.append(cur)
            cur*=10
            for i in range(10):
                dfs(cur+i)
        for i in range(1,10):
            dfs(i)
        return ans
        
            

        
