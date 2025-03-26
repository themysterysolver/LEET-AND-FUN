class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int l=nums.length;
        int median=nums[(int)(l/2)];
        int count=0;
        for(int i:nums){
            count+=Math.abs(median-i);
        }
        return count;
    }
}