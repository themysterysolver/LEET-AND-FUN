class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left=0;
        int right=arr.length-1;
        int mid;
        while(left<right){
            mid=(left+right)/2;
            if(arr[mid-1]<arr[mid] && arr[mid+1]<arr[mid]){
                return mid;
            }
            else if(arr[mid-1]>arr[mid] && arr[mid+1]<arr[mid]){
                right=mid;
            }
            else{
                left=mid;
            }
        }
        return left;
    }
}