class SmallestInfiniteSet {
    private PriorityQueue<Integer> heap;
    private int min;
    public SmallestInfiniteSet() {
        heap=new PriorityQueue<>();
        min=1;
    }
    public int popSmallest() {
        if(!heap.isEmpty()){
            return heap.poll();
        }   
        min++;
        return min-1;
    }
    
    public void addBack(int num) {
        if(min>num && !heap.contains(num)){
            heap.add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */