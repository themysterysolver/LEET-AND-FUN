class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        HashSet<Integer> setA=new HashSet<>();
        HashSet<Integer> setB=new HashSet<>();
        int[] result=new int[A.length];
        for(int i=0;i<A.length;i++){
            setA.add(A[i]);
            setB.add(B[i]);
            HashSet intersection=new HashSet<>(setA);
            intersection.retainAll(setB);
            result[i]=intersection.size();
        }
        return result;
    }
}