class Solution {
    public String reorganizeString(String s) {
        HashMap<Character,Integer> hash_freq=new HashMap<>();
        for(char c:s.toCharArray()){
            hash_freq.put(c,hash_freq.getOrDefault(c,0)+1);
        }
        String result="";
        PriorityQueue<Character> max_heap=new PriorityQueue<>((a,b)->hash_freq.get(b)-hash_freq.get(a));
        max_heap.addAll(hash_freq.keySet());
        while(max_heap.size()>1){
            char c1=max_heap.poll();
            char c2=max_heap.poll();
            result+=c1+""+c2;
            hash_freq.put(c1,hash_freq.get(c1)-1);
            hash_freq.put(c2,hash_freq.get(c2)-1);
            if(hash_freq.get(c1)>0) max_heap.add(c1);
            if(hash_freq.get(c2)>0) max_heap.add(c2);
        }
        if(!max_heap.isEmpty()){
            char c=max_heap.poll();
            if(hash_freq.get(c)>1) return "";
            result+=c;
        }
        return result;
    }
    
}