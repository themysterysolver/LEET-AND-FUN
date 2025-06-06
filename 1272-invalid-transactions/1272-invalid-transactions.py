class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        newTransactions=[]
        invalid=set()
        for t in transactions:
            n,time,amt,city=t.split(',')
            newTransactions.append((n,int(time),int(amt),city,t))
        newTransactions.sort(key=lambda x:x[0])
        for idx,trans in enumerate(newTransactions):
            n1,t1,amt1,city1,trans1=trans
            if amt1>1000:
                invalid.add(trans1)
            for j in range(idx+1,len(newTransactions)):
                n2,t2,amt2,city2,trans2=newTransactions[j]
                if n1==n2:
                    if city1!=city2 and abs(t1-t2)<=60:
                        invalid.add(trans1)
                        invalid.add(trans2)
                else:
                    break
        last=[]
        c=Counter(transactions)
        for t in invalid:
            last+=[t for _ in range(c[t])]
        return last