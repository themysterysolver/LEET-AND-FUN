class Solution {
    public int[] decrypt(int[] code, int k) {
        int result[]=new int[code.length];
        int sum;
        for(int i=0;i<code.length;i++){
            sum=0;
            if(k>0){
                for(int j=i+1;j<i+1+k;j++){
                    sum+=code[j%code.length];
                }
            }
            if(k<0){
                for(int j=i-Math.abs(k);j<i;j++){
                    sum+=code[(j+code.length)%code.length];
                }
            }
            result[i]=sum;
        }
        return result;
    }
}
