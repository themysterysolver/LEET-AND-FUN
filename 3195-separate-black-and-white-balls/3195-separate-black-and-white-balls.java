class Solution {
    public long minimumSteps(String s) {
        long count=0,prev_no_of_zeroes=0;
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i)=='0'){
                prev_no_of_zeroes++;
            }
            else{
                count+=prev_no_of_zeroes;
            }
        }
        return count;
    }
}