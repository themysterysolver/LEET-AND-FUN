class Solution {
    public boolean canConstruct(String s, int k) {
        if(s.length()<k){
            return false;
        }
        Map<Character,Integer> hash=new HashMap<>();
        for(char c:s.toCharArray()){
            hash.put(c,hash.getOrDefault(c,0)+1);
        }
        ArrayList<Integer> val=new ArrayList<>(hash.values());
        int count=0;
        for(int i:val){
            if(i%2==1){
                count++;
            }
        }
        if(count<=k){
            return true;
        }
        else{
            return false;
        }
    }
}