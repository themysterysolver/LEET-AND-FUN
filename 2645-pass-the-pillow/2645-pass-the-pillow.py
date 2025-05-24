class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr=1
        forward=True
        for i in range(time):
            if curr<n and forward:
                curr+=1
            else:
                curr-=1
                forward=False
                if curr==1:
                    forward=True
            print(i,curr)
        return curr
