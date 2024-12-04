class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int j=0;
        for(int i=0;i<str1.length();i++){
            char c1=str1.charAt(i);
            char c2=str2.charAt(j);
            int ascii=(c1-'a'+1)%26;
            if(ascii==c2-'a' || c1==c2){
                j++;
                if(j==str2.length()){
                    return true;
                }
            }
        }
        return false;
    }
}