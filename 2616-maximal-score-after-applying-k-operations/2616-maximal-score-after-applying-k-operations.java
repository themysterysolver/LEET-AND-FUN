class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> heap=new PriorityQueue<>();
        for(int i:nums){
            heap.add(-i);
        }
        System.out.println(heap);
        long score=0;
        for(int i=0;i<k;i++){
            int largest=-heap.poll();
            score+=largest;
            largest=(int)Math.ceil(largest/3.0);
            heap.add(-largest);
        }
        return score;
    }
}