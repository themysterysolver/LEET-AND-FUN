class Solution {
    public int[] minOperations(String boxes) {
        int[] answer=new int[boxes.length()];
        for(int i=0;i<boxes.length();i++){
            int ans=0;
            for(int j=0;j<boxes.length();j++){
                if(i==j){
                    continue;
                }
                else if(boxes.charAt(j)=='1'){
                    ans+=Math.abs(i-j);
                }
            }
            answer[i]=ans;
        }
        return answer;
    }
}