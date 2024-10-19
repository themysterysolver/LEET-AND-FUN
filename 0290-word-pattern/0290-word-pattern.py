class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        print(pattern,'----->',s)
        string=s.split()
        print(string)
        hash=dict()
        i=0
        if len(pattern)!=len(string):
            return False
        for c in pattern:
            if c not in hash:
                hash[c]={string[i]}
                i+=1
            else:
                hash[c].add(string[i])
                i+=1
        print(hash)
        ans_vals=hash.values()
        print(ans_vals)
        for l in ans_vals:
            if len(l)==1:
                continue
            else:
                return False
        ans_val_mul=[]
        for s in ans_vals:
            ans_val_mul+=list(s)
        print(ans_val_mul)
        if len(ans_val_mul)==len(set(ans_val_mul)):
            return True
        else:
            return False