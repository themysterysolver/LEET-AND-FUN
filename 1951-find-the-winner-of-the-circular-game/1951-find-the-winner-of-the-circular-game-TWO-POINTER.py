class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i for i in range(1,n+1)]
        curr = 0
        while len(lst)>1:
            curr = (curr+(k-1))%(len(lst))
            lst.pop(curr)
        return lst[0]
