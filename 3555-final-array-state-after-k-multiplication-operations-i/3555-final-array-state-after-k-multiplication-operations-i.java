class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        int idx;
        ArrayList<Integer> arr=new ArrayList<>();
        for(int i:nums){
            arr.add(i);
        }
        while(k!=0){
            idx=arr.indexOf(min(arr));
            arr.set(idx,arr.get(idx)*multiplier);
            k--;
        }
        for(int i=0;i<nums.length;i++){
            nums[i]=arr.get(i);
        }
        return nums;
    }
    private int min(ArrayList<Integer> arr){
        int mini=Integer.MAX_VALUE;
        for(int n:arr){
            if(n<mini){
                mini=n;
            }
        }
        return mini;
    }
}