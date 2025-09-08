class Solution {
    public boolean isValid(int n){
        String s = String.valueOf(n);
        return !s.contains("0");
    }
    public int[] getNoZeroIntegers(int n) {
        for(int i=1;i<n+1;i++){
            if(isValid(i) && isValid(n-i)){
                return new int[]{i,n-i};
            } 
        }
        return new int[]{};
    }
}