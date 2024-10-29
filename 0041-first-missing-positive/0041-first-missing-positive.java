class Solution {
    public int firstMissingPositive(int[] nums) {
        Map<Integer,Boolean> map=new HashMap<>();
        long maxi=0;
        for(int i:nums){
            if(i<=0){
                continue;
            }else{
                map.put(i,true);
                maxi=Math.max(maxi,i);
            }
        }
        for(int i=1;i<maxi+1;i++){
            if(!map.containsKey(i)){
                return i;
            }
        }
        return (int)maxi+1;
    }
}