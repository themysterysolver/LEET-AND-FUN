class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        Map<String,Integer> freq=new HashMap<>();
        for(int[] row:matrix){
            StringBuilder pattern=new StringBuilder("");
            for(int i=0;i<row.length;i++){
                if(row[0]==row[i]){
                    pattern.append("T");
                }
                else{
                    pattern.append("F");
                }
            }
            freq.put(pattern.toString(),freq.getOrDefault(pattern.toString(),0)+1);
        }
        return Collections.max(freq.values());
    }
}