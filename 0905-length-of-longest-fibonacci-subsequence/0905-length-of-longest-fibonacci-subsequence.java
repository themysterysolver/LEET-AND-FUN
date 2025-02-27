class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        int maxi=0;
        Set<Integer> hash=new HashSet<>();
        for(int i:arr){
            hash.add(i);
        }
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                int count=2;
                int prev=arr[j];
                int curr=arr[i]+arr[j];
                while(hash.contains(curr)){
                    count++;
                    int temp=curr;
                    curr+=prev;
                    prev=temp;
                    maxi=Math.max(maxi,count);
                }
            }
        }
        return maxi;
    }
}