class Solution {
    public int largestCombination(int[] candidates) {
        ArrayList<Integer> setBit=new ArrayList<>(24);
        for (int i = 0; i < 24; i++) {
            setBit.add(0); 
        }
        System.out.println(setBit);
        for(int num:candidates){
            for(int i=0;i<24;i++){
                if((num&(1<<i))!=0){
                    setBit.set(i,setBit.get(i)+1);
                }
            }
        }
        return Collections.max(setBit);
    }
}
