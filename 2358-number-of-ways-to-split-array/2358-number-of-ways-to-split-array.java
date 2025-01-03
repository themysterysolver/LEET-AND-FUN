class Solution {
    public int waysToSplitArray(int[] nums) {
        int l=nums.length;
        long[] prefixSum=new long[l];
        long[] suffixSum=new long[l];
        long prefix=0,suffix=0;
        for(int i=0;i<l;i++){
            prefix+=nums[i];
            prefixSum[i]=prefix;
        }
        for(int i=l-1;i>-1;i--){
            suffix+=nums[i];
            suffixSum[i]=suffix;
        }
        int count=0;
        for(int i=0;i<l-1;i++){
            if(prefixSum[i]>=suffixSum[i+1]){
                count++;
            }
        }
        return count;
    }
}