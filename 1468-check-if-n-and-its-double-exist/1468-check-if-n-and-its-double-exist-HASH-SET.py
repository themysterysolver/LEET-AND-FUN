class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrSet=set()
        for num in arr:
            if num*2 in arrSet or (num%2==0 and num//2 in arrSet):
                return True
            arrSet.add(num)
        return False
