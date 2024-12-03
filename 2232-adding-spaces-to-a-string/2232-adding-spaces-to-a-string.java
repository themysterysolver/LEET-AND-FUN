class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder ds=new StringBuilder();
        int prev=0;
        for(int i:spaces){
            ds.append(s.substring(prev,i)).append(" ");
            prev=i;
        }
        ds.append(s.substring(prev));
        return ds.toString();
    }
}