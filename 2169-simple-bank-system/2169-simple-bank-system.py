class Bank:

    def __init__(self, balance: List[int]):
        self.bal = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1-=1
        account2-=1
        if 0<=account1<self.n and 0<=account2<self.n and self.bal[account1]>=money:
            self.bal[account2]+=money
            self.bal[account1]-=money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        account-=1
        if 0<=account<self.n:
            self.bal[account]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        if 0<=account<self.n and self.bal[account]>=money:
            self.bal[account]-=money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)