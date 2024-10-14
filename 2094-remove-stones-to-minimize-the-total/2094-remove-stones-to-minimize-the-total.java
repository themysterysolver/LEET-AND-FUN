class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for(int i:piles){
            pq.add(-i);
        }
        int sum=0;
        for(int i=0;i<k;i++){
            int largest=-pq.poll();
            pq.add(-(largest-largest/2));
        }
        while(!pq.isEmpty()){
            sum+=-pq.poll();
        }
        return sum;
    }
}