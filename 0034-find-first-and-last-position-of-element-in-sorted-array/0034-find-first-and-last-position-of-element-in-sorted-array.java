class Solution {
    public int leftMost(int[] nums,int target){
        int index=-1,mid;
        int start=0,end=nums.length-1;
        while(start<=end){
            mid=(start+end)/2;
            if(nums[mid]==target){
                index=mid;
                end=mid-1;
            }
            else if(nums[mid]<target){
                start=mid+1;
            }
            else{
                end=mid-1;
            } 
        }
        return index;
    }
    public int rightMost(int[] nums,int target){
        int index=-1,mid;
        int start=0,end=nums.length-1;
        while(start<=end){
            mid=(start+end)/2;
            if(nums[mid]==target){
                index=mid;
                start=mid+1;
            }
            else if(nums[mid]<target){
                start=mid+1;
            }
            else{
                end=mid-1;
            } 
        }
        return index;
    }
    public int[] searchRange(int[] nums, int target) {
        int[] result=new int[2];
        result[0]=leftMost(nums,target);
        result[1]=rightMost(nums,target);
        return result;
    }
}