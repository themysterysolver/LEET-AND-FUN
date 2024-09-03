class Solution:
    def display(self,a):
        for i in a:
            print(i)
        print('---------------------------')
    def minPathSum(self, grid: List[List[int]]) -> int:
        a=grid
        sumi=0
        self.display(a)
        for i in range(len(a[0])):
            sumi+=a[0][i]
            a[0][i]=sumi
        self.display(a)
        for i in range(1,len(a)):
            for j in range(len(a[i])):
                if j==0:
                    a[i][j]=a[i][j]+a[i-1][j]
                else:
                    a[i][j]=a[i][j]+min(a[i][j-1],a[i-1][j])
        self.display(a)
        return a[-1][-1]