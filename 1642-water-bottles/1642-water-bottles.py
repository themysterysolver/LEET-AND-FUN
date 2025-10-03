class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        full,empty = numBottles,0
        while full>0:
            drink+=numBottles
            empty+=numBottles
            full = empty//numExchange
            numBottles = full
            empty-=numExchange*full
        return drink