class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        vcut,hcuts=0,0
        row,col=[],[]
        for startx,starty,endx,endy in rectangles:
            row.append([starty,endy])
            col.append([startx,endx])
        row.sort()
        col.sort()
        #print("AT ROW:",row)
        #print("AT COL:",col)
        mrow=[]
        for x,y in row:
            if not mrow:
                mrow.append([x,y])
            else:
                if x<mrow[-1][-1]:
                    if y>mrow[-1][-1]:
                        mrow[-1][-1]=y
                else:
                    mrow.append([x,y])
        mcol=[]
        for x,y in col:
            if not mcol:
                mcol.append([x,y])
            else:
                if x<mcol[-1][-1]:
                    if y>mcol[-1][-1]:
                        mcol[-1][-1]=y
                else:
                    mcol.append([x,y])
        #print("MROW:",mrow)
        #print("MCOL:",mcol)
        return len(mrow)>2 or len(mcol)>2