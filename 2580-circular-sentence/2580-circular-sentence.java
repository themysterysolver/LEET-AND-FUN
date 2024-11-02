class Solution {
    public boolean isCircularSentence(String sentence) {
        String[] word=sentence.split("\\s+");
        for(int i=0;i<word.length-1;i++){
            if(word[i].charAt(word[i].length()-1)==word[i+1].charAt(0)){
                continue;
            }
            else{
                return false;
            }
        }
        return word[0].charAt(0)==word[word.length-1].charAt(word[word.length-1].length()-1)? true:false;
    }
}