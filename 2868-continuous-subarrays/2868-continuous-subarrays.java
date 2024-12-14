class Solution {
    public long continuousSubarrays(int[] nums) {
        long count=0;
        int start=0,end=0;
        HashMap<Integer,Integer> hash=new HashMap<>();
        while(end<nums.length){
            hash.put(nums[end],hash.getOrDefault(nums[end],0)+1);
            while(Collections.max(hash.keySet())-Collections.min(hash.keySet())>2){
                hash.put(nums[start],hash.get(nums[start])-1);
                if(hash.get(nums[start])==0){
                    hash.remove(nums[start]);
                }
                start++;
            }
            count+=end-start+1;
            end++;
        }
        return count;
    }
}