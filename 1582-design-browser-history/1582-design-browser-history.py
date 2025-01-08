class Node:
    def __init__(self,data=None):
        self.val=data
        self.next=None
        self.prev=None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.current=Node(homepage)
    def visit(self, url: str) -> None:
        newNode=Node(url)
        newNode.prev=self.current
        self.current.next=newNode
        self.current=newNode
    def back(self, steps: int) -> str:
        while self.current.prev and steps!=0:
            self.current=self.current.prev
            steps-=1
        print('at back:',self.current.val)
        return self.current.val
    def forward(self, steps: int) -> str:
        while self.current.next and steps!=0:
            self.current=self.current.next
            steps-=1
        print('at forawd:',self.current.val)
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)