class Solution {
    public int firstMissingPositive(int[] nums) {
        List<Integer> num=new ArrayList<>();
        for(int i:nums){
            num.add(i);
        }
        Set<Integer> set=new HashSet<>(num);
        num=new ArrayList<>(set);
        int current=1;
        Collections.sort(num);
        for(int i:num){
            if(i<=0){
                continue;
            }
            else if(i!=current){
                return current;
            }
            else{
                current++;
            }
        }
        return current;
    }
}