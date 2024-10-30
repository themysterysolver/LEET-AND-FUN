class Solution {
    public int findPeakElement(int[] nums) {
        int left=0;
        int right=nums.length-1;
        int mid;
        while(left<=right){
            mid=(left+right)/2;
            if(mid!=0 && mid!=nums.length-1){
                if(nums[mid-1]<nums[mid] && nums[mid+1]<nums[mid]){
                    return mid;
                }
                else if(nums[mid+1]>nums[mid]){
                    left=mid+1;
                }
                else if(nums[mid-1]>nums[mid]){
                    right=mid-1;
                }
            }
            else{
                if(nums.length==1){
                    return 0;
                }
                if(mid==0){
                  if(nums[mid+1]<nums[mid]){
                    return 0;
                  }
                  else{
                    left=mid+1;
                  }  
                }
                else if(mid==nums.length-1){
                    if(nums[mid-1]<nums[mid]){
                        return nums.length-1;
                    }
                    else{
                        right=mid-1;
                    }
                }
            }
        }
        return left;
    }
}
