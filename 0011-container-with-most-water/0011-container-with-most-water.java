class Solution {
    public int maxArea(int[] height) {
        int start=0,end=height.length-1;
        int max_area=Math.min(height[end],height[start])*(end-start);
        while (start<end){
            if(height[start]<height[end]){
                start++;
            }
            else{
                end--;
            }
            max_area=Math.max(Math.min(height[end],height[start])*(end-start),max_area);
        }
        return max_area;
    }
}