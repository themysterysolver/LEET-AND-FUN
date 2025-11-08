class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g,p,m = 0,0,0
        l1,l2,l3 = -1,-1,-1 #last seen
        for i in range(len(garbage)):
            c = Counter(garbage[i])
            for el in 'GMP':
                if el in c and el == 'G':
                    g+=c[el]
                    l1=i
                if el in c and el == 'M':
                    m+=c[el]
                    l2=i
                if el in c and el == 'P':
                    p+=c[el]
                    l3=i
        #print(g,p,m)
        if l1!=-1:
            g+=sum(travel[:l1])
        if l2!=-1:
            m+=sum(travel[:l2])
        if l3!=-1:
            p+=sum(travel[:l3])
        return g+p+m