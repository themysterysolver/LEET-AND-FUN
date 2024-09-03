class Solution:
    def display(self,a):
        for i in a:
            print(i)
        print('---------------------------')
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        a= obstacleGrid
        if a[0][0]==1 or a[-1][-1]==1:
            return 0
        #obstacle to -1
        for i in range(len(obstacleGrid)):
            for j in range(len(a[i])):
                if a[i][j]==1:
                    a[i][j]=-1
        self.display(a)
        flag=0
        #top to obstacle
        for i in range(len(a[0])):
            if a[0][i]!=-1:
                a[0][i]=1
            if a[0][i]==-1:
                a[0][i]=0
                flag=1
            if flag==1:
                a[0][i]=0
        self.display(a)
        flag=0
        #right to obstcale
        for i in range(len(a)):
            if a[i][0]!=-1:
                a[i][0]=1
            if a[i][0]==-1:
                a[i][0]=-1
                flag=1
            if flag==1:
                a[i][0]=-1
        self.display(a)
        #main logic
        for i in range(1,len(a)):
            for j in range(1,len(a[i])):
                if a[i][j]==-1:
                    continue
                if a[i-1][j]==-1 and a[i][j-1]==-1:
                    a[i][j]=0
                elif a[i-1][j]==-1:
                    a[i][j]=a[i][j-1]
                elif a[i][j-1]==-1:
                    a[i][j]=a[i-1][j]
                else:
                    a[i][j]=a[i-1][j]+a[i][j-1]
        self.display(a)
        return a[-1][-1]