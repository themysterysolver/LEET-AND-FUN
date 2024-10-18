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
    public List<List<Integer>> subsets(int[] nums) {
            List<List<Integer>> result=new ArrayList<>();
            helper(nums,result,new ArrayList<>(),0);
            return result;
    }
}
