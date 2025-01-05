class Solution {
    public String shiftingLetters(String str, int[][] shifts) {
        int l=str.length();
        char[] s=str.toCharArray();
        int[] toDo=new int[l+1];
        for(int i=0;i<shifts.length;i++){
            int start=shifts[i][0];
            int end=shifts[i][1];
            int action=shifts[i][2];
            if(action==0){
                toDo[start]-=1;
                toDo[end+1]+=1;
            }else{
                toDo[start]+=1;
                toDo[end+1]-=1;
            }
        }
        int shift=0;
        for(int i=0;i<toDo.length;i++){
            shift+=toDo[i];
            toDo[i]=shift;
        }
        StringBuilder result=new StringBuilder();
        for(int i=0;i<l;i++){
            int nc=((s[i]-'a'+toDo[i])%26);
            if(nc<0)nc+=26;
            result.append((char)(nc+'a'));
        }
        return result.toString();
    }
}