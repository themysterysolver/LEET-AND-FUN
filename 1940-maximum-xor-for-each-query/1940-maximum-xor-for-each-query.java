class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        ArrayList<Integer> prefixXOR=new ArrayList<>();
        prefixXOR.add(nums[0]);
        int[] answer=new int[nums.length];
        for(int i=1;i<nums.length;i++){
            prefixXOR.add(prefixXOR.get(i-1)^nums[i]);
        }
        int mask=(1<<maximumBit)-1;
        for(int i=prefixXOR.size()-1;i>-1;i--){
            answer[nums.length-1-i]=prefixXOR.get(i)^mask;
        }
        return answer;
    }
}