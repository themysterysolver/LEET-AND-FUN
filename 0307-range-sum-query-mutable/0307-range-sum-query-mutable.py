class segmentTree:
    def display(self):
        print(self.tree)
    
    def __init__(self,nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0]*(4*self.n)
        self.build(0,0,self.n-1,nums)
        self.display()

    def build(self,currI,l,r,arr):
        if l == r:
            self.tree[currI] = arr[l]
        else:
            mid = (l+r)//2
            left = 2*currI + 1
            right = 2*currI + 2
            self.build(left,l,mid,arr)
            self.build(right,mid+1,r,arr)
            self.tree[currI] = self.tree[left] + self.tree[right]
    
    def getSum(self,left,right):
        return self.sumIt(0,0,self.n-1,left,right)
    
    def sumIt(self,idx,sl,sr,l,r): #sl => segment tree left and sr+> segment tree right
        if r<sl or sr<l:
            return 0
            
        if l<=sl and sr<=r:
            return self.tree[idx]

        mid = (sl+sr)//2
        return self.sumIt(idx*2+1,sl,mid,l,r)+self.sumIt(idx*2+2,mid+1,sr,l,r)

    def updateIt(self,index,val):
        curr = self.nums[index]
        diff = val - curr
        self.nums[index]+=diff
        self.update(0,0,self.n-1,index,diff)
    
    def update(self,idx,sl,sr,pos,diff):
        if sl>pos or sr<pos:
            return
        self.tree[idx] += diff
        if sl!=sr:
            mid = (sl+sr) // 2
            self.update(idx*2+1,sl,mid,pos,diff)
            self.update(idx*2+2,mid+1,sr,pos,diff)    
    

    
class NumArray:
    def __init__(self, nums: List[int]):
        self.st = segmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.updateIt(index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.getSum(left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)