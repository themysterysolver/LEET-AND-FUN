class Solution {
    public String longestDiverseString(int a, int b, int c) {
        HashMap<Character,Integer> frequency=new HashMap<>();
        if(a>0) frequency.put('a',a);
        if(b>0) frequency.put('b',b);
        if(c>0) frequency.put('c',c);
        System.out.println(frequency);
        PriorityQueue<Character> maxHeap=new PriorityQueue<>((p,q)->frequency.get(q)-frequency.get(p));
        maxHeap.addAll(frequency.keySet());
        System.out.println(maxHeap);
        String result="";
        while(!maxHeap.isEmpty()){
            char c1=maxHeap.poll();
            if(result.length()>=2 && result.charAt(result.length()-1)==c1 && result.charAt(result.length()-2)==c1){
                if(maxHeap.isEmpty())break;
                char c2=maxHeap.poll();
                result+=c2;
                frequency.put(c2,frequency.get(c2)-1);
                if(frequency.get(c2)>0) maxHeap.add(c2);
                maxHeap.add(c1);
            }
            else{
                result+=c1;
                frequency.put(c1,frequency.get(c1)-1);
                if(frequency.get(c1)>0) maxHeap.add(c1);
            }
        }
        return result;
    }
}