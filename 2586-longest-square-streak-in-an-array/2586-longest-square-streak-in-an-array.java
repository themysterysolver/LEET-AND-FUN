class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        int maxlen=0,sqrt=0;
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int n:nums){
            sqrt=(int)Math.sqrt(n);
            if(sqrt*sqrt==n && map.containsKey(sqrt)){
                map.put(n,map.get(sqrt)+1);
                maxlen=Math.max(maxlen,map.get(n));
            }
            else{
                map.put(n,1);
            }
        }
        return maxlen>=2?maxlen:-1;
    }
}