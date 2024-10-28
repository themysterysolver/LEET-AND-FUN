class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        int maxlen=0,len=0;
        Set<Integer> visited=new HashSet<>();
        Set<Integer> checker=new HashSet<>();
        for(int i:nums){
            checker.add(i);
        }
        for(int n:nums){
            int num=n;
            len=1;
            while(checker.contains(num*num) && !visited.contains(num*num)){
                visited.add(num*num);
                num=num*num;
                len++;
            }
            maxlen=Math.max(maxlen,len);
        }
        return maxlen>=2?maxlen:-1;
    }
}
