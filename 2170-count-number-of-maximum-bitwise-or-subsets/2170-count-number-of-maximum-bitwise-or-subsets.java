class Solution {
    public void helper(int[] nums,List<List<Integer>> result,List<Integer> subset,int n){
        if(n==nums.length){
            result.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[n]);
        helper(nums,result,subset,n+1);
        subset.remove(subset.size()-1);
        helper(nums,result,subset,n+1);
    }
    public int calculateMaxOrSubset(List<List<Integer>> result){
        int max_or_value=0,count=0;
        for(List<Integer> counter:result){
            int subset_or=0;
            for(int num:counter){
                subset_or |=num;
            }
            if(subset_or>max_or_value){
                count=1;
                max_or_value=subset_or;
            }
            else if(max_or_value==subset_or){
                count++;
            }
        }
        return count;
    }
    public int countMaxOrSubsets(int[] nums) {
            List<List<Integer>> result=new ArrayList<>();
            helper(nums,result,new ArrayList<>(),0);
            return calculateMaxOrSubset(result);
    }
}