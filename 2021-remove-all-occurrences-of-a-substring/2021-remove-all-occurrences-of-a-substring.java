class Solution {
    public String removeOccurrences(String s, String part) {
        int l=part.length();
        while(s.contains(part)){
            int idx=s.indexOf(part);
            s=s.substring(0,idx)+s.substring(idx+l);
        }
        return s;
    }
}