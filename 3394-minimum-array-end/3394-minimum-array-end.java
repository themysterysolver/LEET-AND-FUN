class Solution {
    public long minEnd(int n, int x) {
        long result=x;
        while(n>1){
            result=(result+1)|x;
            n--;
        }
        return result;
    }
}