class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int start=0,size=0;
        long sum=0,max=0;
        HashMap<Integer,Integer> hash=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            hash.put(nums[i],hash.getOrDefault(nums[i],0)+1);
            size++;
            sum+=nums[i];
            while(size>k){
                hash.put(nums[start],hash.get(nums[start])-1);
                if(hash.get(nums[start])==0){
                    hash.remove(nums[start]);
                }
                size--;
                sum-=nums[start];
                start++;
            }
            if(size==k && hash.size()==k){
                max=Math.max(max, sum);
            }
        }
        return max;
    }
}