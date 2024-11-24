class Solution {
    public long maxMatrixSum(int[][] matrix) {
        int negativecount=0;
        long sum=0;
        long minAbs=Long.MAX_VALUE;
        for(int[] row:matrix){
            for(int i:row){
                sum+=Math.abs(i);
                if(i<0)negativecount++;
                minAbs=Math.min(minAbs,Math.abs(i));
            }
        }
        if(negativecount%2==1)sum-=2*minAbs;
        return sum;
    }
}