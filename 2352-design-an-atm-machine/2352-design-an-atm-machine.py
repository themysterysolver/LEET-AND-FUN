class ATM:
    def __init__(self):
        self.idx = [20,50,100,200,500]
        self.bal = [0,0,0,0,0]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.bal[i]+=banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        take=[0]*5
        for i in range(4,-1,-1):
            take[i] = min(self.bal[i],amount//self.idx[i])
            amount -= self.idx[i]*take[i]

        if amount == 0:
            for i in range(5):
                self.bal[i]-=take[i]
            return take
        return [-1]
                

             
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)