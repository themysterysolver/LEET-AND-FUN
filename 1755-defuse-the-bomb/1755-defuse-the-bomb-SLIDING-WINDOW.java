class Solution {
    public int[] decrypt(int[] code, int k) {
        int result[]=new int[code.length];
        int start=1,end=k,windowSum=0;
        if(k<0){
            start=code.length-Math.abs(k);
            end=code.length-1;
        }
        for(int i=start;i<end+1;i++){
            windowSum+=code[i];
        }
        for(int i=0;i<code.length;i++){
            result[i]=windowSum;
            windowSum-=code[start%code.length];
            windowSum+=code[(end+1)%code.length];
            start++;
            end++;
        }
        System.out.println(windowSum);
        return result;
    }
}
