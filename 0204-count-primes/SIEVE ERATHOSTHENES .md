## SIEVE OF ERATHROSTHENES
- Used to find all number up to a given element
```python3[]
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        l=[True]*n   
        l[0]=l[1]=False
        for i in range(2,int(n**0.5)+1):
            if l[i]:
                for j in range(i*i,n,i):
                    l[j]=False
            i=i+1
        return sum(l)
```
- why $\sqrt{n}$ ,coz greater than that would be marked by smaller elements by multiples of `i`.
- why $i^2$,coz same reason,small elemtns less than `i*i` would have already been makred my buiples lass than it.
