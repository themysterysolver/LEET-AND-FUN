import java.util.Arrays;
class Solution {
    public int longestOnes(int[] nums,int k) {
        int zeros_flipped=0,max=0,start=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                zeros_flipped++;
            }
            while(zeros_flipped>k){
                if(nums[start]==0){
                    zeros_flipped--;
                }
                start++;
            }
            max=Math.max(max,i-start+1);
        }
        return max;
    }
}
