class Solution {
    public boolean isArraySpecial(int[] nums) {
       int l=nums.length;
       for(int i=0;i<l-1;i++){
        if(nums[i]%2!=nums[i+1]%2){
            continue;
        }
        else{
            return false ;
        }
       }
       return true;
    }
}