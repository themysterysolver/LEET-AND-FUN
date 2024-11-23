class Solution {
    public char[][] rotateTheBox(char[][] box) {
        for(char[] row:box){
            for(int start=0;start<row.length;start++){
                if(row[start]=='#'){
                    int index=row.length-1;
                    for(int end=start+1;end<row.length;end++){
                        if(row[end]=='*'){
                            index=start;
                            break;
                        }
                        else if(row[end]=='.'){
                            index=end;
                            break;
                        }
                    }
                    char temp=row[index];
                    row[index]=row[start];
                    row[start]=temp;
                }
            }
        }
        char[][] newBox=new char[box[0].length][box.length];
        for(int i=0;i<box.length;i++){
            for(int j=0;j<box[0].length;j++){
                newBox[j][box.length-1-i]=box[i][j];
            }
        }
        return newBox;
    }
}