class Solution {
    public int[] flipIt(int[] row){
        int[] flipped=new int[row.length];
        for(int i=0;i<row.length;i++){
            flipped[i]=1-row[i];
        }
        return flipped;
    }
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        int maxIdenticalRows=0;
        for(int[] row:matrix){
            int[] flipped=flipIt(row);
            int count=0;
            for(int[] compareRow:matrix){
                if(Arrays.equals(compareRow,row)||Arrays.equals(compareRow,flipped)){
                    count++;
                }
            }
            maxIdenticalRows=Math.max(count,maxIdenticalRows);
        }
        return maxIdenticalRows;
    }
}
