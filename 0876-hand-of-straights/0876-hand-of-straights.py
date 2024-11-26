class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hash=dict()
        for num in hand:
            hash[num]=hash.get(num,0)+1
        l=len(hand)
        while l>0:
            mini=min(hash.keys())
            for i in range(groupSize):
                if hash.get(mini+i)!=None:
                    hash[mini+i]-=1
                    if hash[mini+i]==0:
                        del hash[mini+i]
                else:
                    return False
                l-=1
        return True