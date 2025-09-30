class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        idx = 0
        cand = 1
        while candies>0:
            res[idx]+=min(cand,candies)
            candies-=cand
            if candies<0:
                break
            cand+=1
            idx = (idx+1) % num_people
        return res