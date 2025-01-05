class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int[] toDo=new int[s.length()];
        int shift=0;
        for(int i=s.length()-1;i>-1;i--){
            shift=(shift+shifts[i])%26;
            toDo[i]=shift;
        }
        StringBuilder result=new StringBuilder();
        char[] str=s.toCharArray();
        for(int i=0;i<s.length();i++){
            result.append((char)((str[i]-'a'+toDo[i])%26+'a'));
        }
        return result.toString();
    }
}