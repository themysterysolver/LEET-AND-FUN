class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int count=0;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                int sum=nums[i]+nums[j];
                for(int k=j+1;k<nums.length && nums[k]<sum;k++){   
                    count++;
                }
            }
        }
        return count;
    }
}