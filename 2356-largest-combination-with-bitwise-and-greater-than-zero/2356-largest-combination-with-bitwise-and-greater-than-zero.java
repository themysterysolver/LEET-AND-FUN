class Solution {
    public int largestCombination(int[] candidates) {
        int maxCount=0,count;
        //System.out.println(setBit);
        for(int i=0;i<24;i++ ){
            count=0;
            for(int num:candidates){
                if((num&(1<<i))!=0){
                    count++;
                }
                maxCount=Integer.max(count,maxCount);
            }
        }
        return maxCount;
    }
}