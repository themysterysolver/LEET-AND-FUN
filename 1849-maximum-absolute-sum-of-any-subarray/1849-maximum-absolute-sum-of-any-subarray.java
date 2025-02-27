class Solution {
    public int kadane(int[] nums){
        int maxi=Integer.MIN_VALUE;
        int sumi=0;
        for(int i:nums){
            sumi+=i;
            maxi=Math.max(maxi,sumi);
            if(sumi<0){
                sumi=0;
            }
        }
        return maxi;
    }
    public int maxAbsoluteSum(int[] nums) {
        int[] nnums=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            nnums[i]=nums[i]*-1;
        }
        return Math.max(kadane(nums),kadane(nnums));
    }
}