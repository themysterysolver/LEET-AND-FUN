class Solution {
    public int[] arrayRankTransform(int[] arr) {
       int[] rank=new int[arr.length];
       ArrayList<Integer> rank_pos=new ArrayList<>();
       HashSet<Integer> unique=new HashSet<>();
       for(int num:arr){
            unique.add(num);
       }
       for(int num:unique){
            rank_pos.add(num);
       }
       Collections.sort(rank_pos);
       System.out.println("unique:"+unique+"\nrank_pos:"+rank_pos);
       HashMap<Integer,Integer> mappi=new HashMap<>();
       for(int i=0;i<rank_pos.size();i++){
            mappi.put(rank_pos.get(i),i+1);
       }
       for(int i=0;i<arr.length;i++){
            rank[i]=mappi.get(arr[i]);
       }
       return rank;
    }
}