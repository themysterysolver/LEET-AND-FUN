class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        int maxlen=0,len=0,num;
        Set<Integer> numss=new HashSet<>();
        for(int i:nums){
            numss.add(i);
        }
        for(int n:nums){
            num=n;
            len=1;
            while(numss.contains(num*num)){
                num*=num;
                len++;
            }
            maxlen=Math.max(maxlen,len);
        }
        return maxlen>=2?maxlen:-1;
    }
}
