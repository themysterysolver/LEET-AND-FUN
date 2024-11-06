class Solution {
    public boolean canSortArray(int[] nums) {
        HashMap<Integer,Integer> hash=new HashMap<>();
        for(int n:nums){
            hash.put(n,Integer.bitCount(n));
        }
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length-1-i;j++){
                if(nums[j+1]<nums[j]){
                    if(hash.get(nums[j+1])==hash.get(nums[j])){
                        int temp=nums[j];
                        nums[j]=nums[j+1];
                        nums[j+1]=temp;
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        return true;
    }
}