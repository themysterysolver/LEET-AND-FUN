class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag = [False]*3
        p,q,r = target
        for a,b,c in triplets:
            if a<=p and b<=q and c<=r:
                if a == p:
                    flag[0] = True
                if b == q:
                    flag[1] = True
                if c == r:
                    flag[-1] = True
        return all(flag)