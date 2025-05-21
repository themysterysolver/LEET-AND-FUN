class NumMatrix:
    def display(self,mat):
        for row in mat:
            print(row)
        print('-----------')
    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix),len(matrix[0])
        self.prefix=[[0]*col for _ in range(row)]

        self.prefix[0][0]=matrix[0][0]
        #self.display(self.prefix)

        for i in range(1,row):
            self.prefix[i][0]=self.prefix[i-1][0]+matrix[i][0]
        #self.display(self.prefix)

        for j in range(1,col):
            self.prefix[0][j]=self.prefix[0][j-1]+matrix[0][j]
        #self.display(self.prefix)

        for i in range(1,row):
            for j in range(1,col):
                self.prefix[i][j]=self.prefix[i-1][j]+self.prefix[i][j-1]+matrix[i][j]-self.prefix[i-1][j-1]
        #self.display(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        end=self.prefix[row2][col2]
        left=0
        right=0
        top=0
        if row1-1>=0 and col1-1>=0:
            top=self.prefix[row1-1][col1-1]
        #print("TOP:{}".format(top))
        if row1-1>=0:
            right=self.prefix[row1-1][col2]
        if col1-1>=0:
            left=self.prefix[row2][col1-1]
        #print("LEFT:{}".format(left))
        #print("RIGHT:{}".format(right))
        #print("End of loop")
        return end+top-left-right


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)