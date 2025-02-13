class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> heap=new PriorityQueue<>();
        for(int num:nums){
            heap.add((long)num);
        }
        Long x,y;
        int count=0;
        while(heap.peek()<k){
            x=heap.poll();
            y=heap.poll();
            heap.add(Math.min(x,y)*2+Math.max(x,y));
            count++;
        }
        return count;
    }
}