class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash = defaultdict(int)
        for num in cpdomains:
            n,d = num.split(' ')
            hash[d]+=int(n)
            a = d.split('.')
            if len(a) == 3:
                x,y,z = a
                hash[z]+=int(n)
                hash[y+"."+z]+=int(n)
            else:
                x,y = a
                hash[y]+=int(n)
        ans = []
        for k,v in hash.items():
            ans.append(str(v)+" "+k)
        return ans