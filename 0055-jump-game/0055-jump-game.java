class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length==1){
            return true;
        }
        int gasoline=nums[0];
        for(int i=1;i<nums.length-1;i++){
            gasoline--;
            if(gasoline==-1){
                return false;
            }
            if(gasoline<nums[i]){
                gasoline=nums[i];
            }
        }
        if(gasoline>=1){
            return true;
        }
        else{
            return false;
        }
    }
}