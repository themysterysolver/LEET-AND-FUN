class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def rev(x):
            return 'R' if x=='D' else 'D'
        q=list(senate)
        while len(q)!=1:
            s=q.pop(0)
            if rev(s) in set(q):
                idx=q.index(rev(s))
                q.pop(idx)
            else:
                return 'Radiant' if s=='R' else 'Dire'
            q.append(s)
        return 'Radiant' if q[0]=='R' else 'Dire'