class Solution {
    public boolean canSortArray(int[] nums) {
        int minSeg=nums[0],maxSeg=nums[0];
        int maxPrev=Integer.MIN_VALUE;
        int setBits=Integer.bitCount(nums[0]);
        for(int i=1;i<nums.length;i++){
            if(Integer.bitCount(nums[i])==setBits){
                maxSeg=Math.max(maxSeg,nums[i]);
                minSeg=Math.min(minSeg,nums[i]);
            }
            else{
                if(minSeg<maxPrev){
                    return false;
                }
                else{
                    maxPrev=maxSeg;
                    minSeg=nums[i];
                    maxSeg=nums[i];
                    setBits=Integer.bitCount(nums[i]);
                }
            }
        }
        if(minSeg<maxPrev){
            return false;
        }
        return true;
    }
}