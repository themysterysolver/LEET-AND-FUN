import java.util.ArrayList;
import java.util.List;
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum=0;
        double maxsum=Integer.MIN_VALUE;
        List<Integer> arr=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
           arr.add(nums[i]);
           sum+=nums[i];
           if(arr.size()==k){
                maxsum=Math.max(maxsum,sum);
                sum=sum-arr.remove(0);
           }
        }
        return maxsum/k;
    }
}