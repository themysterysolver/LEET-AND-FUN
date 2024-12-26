class Solution {
    private int count;
    public Solution(){
        count=0;
    }
    public void permuation(int[] nums,int cidx,int csum,int target){
        if(cidx==nums.length){
            if(csum==target){
                count+=1;
            }
        }else{
            permuation(nums,cidx+1,csum+nums[cidx],target);
            permuation(nums,cidx+1,csum-nums[cidx],target);
        }
    }
    public int findTargetSumWays(int[] nums, int target) {
        permuation(nums,0,0,target);
        return count;    
    }
}