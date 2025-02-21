# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.setter=set()
        def dis(result):
            for t in result:
                if t!=-1:
                    print(t.val,end='')
                    self.setter.add(t.val)
                else:
                    pass
                    #print('\n-----------')
            #print('***********************************************') 
        def display(r):
            result=[]
            q=deque([(r)])
            while q:
                l=len(q)
                for _ in range(l):
                    n=q.popleft()
                    result.append(n)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                result.append(-1)
            dis(result)
        def build(r):
            if r:
                if r.left:
                    r.left.val=2*r.val+1
                    build(r.left)
                if r.right:
                    r.right.val=2*r.val+2
                    build(r.right)
        if root:
            root.val=0 
            build(root)
        display(root)
    def find(self, target: int) -> bool:
        return True if target in self.setter else False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)