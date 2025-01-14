class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        Map<Integer,Integer> hash=new HashMap<>();
        int[] result=new int[A.length];
        for(int i=0;i<A.length;i++){
            hash.put(A[i],hash.getOrDefault(A[i],0)+1);
            hash.put(B[i],hash.getOrDefault(B[i],0)+1);
            int count=0;
            if(hash.get(A[i])==2){
                count++;
            }
            if(hash.get(B[i])==2 && A[i]!=B[i]){
                count++;
            }
            if(i==0){
                result[i]=count;
            }else{
                result[i]=count+result[i-1];
            }
        }
        return result;
    }
}