class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def display(mat):
            for row in mat:
                print(row)
            print('-----------------------')
        #display(box)
        for row in box:
            for start in range(len(row)):
                if row[start]=='#':
                    index=len(row)-1
                    for end in range(start+1,len(row)):
                        if row[end]=='*':
                            index=start
                            break
                        if row[end]=='.':
                            index=end
                            break
                    row[start],row[index]=row[index],row[start]
        #display(box)
        newBox=[['']*len(box) for _ in range(len(box[0]))]
        #display(newBox)
        for i in range(len(box)):
            for j in range(len(box[0])):
                newBox[j][len(box)-1-i]=box[i][j]
            print('----------------------------')
        #display(newBox)
        return newBox
