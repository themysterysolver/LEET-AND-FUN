import java.util.regex.*;
class Solution {
    public boolean isValid(String word) {
        return (word.length()>=3 && word.matches("[A-Za-z0-9]+") && Pattern.compile("[aeiouAEIOU]").matcher(word).find() && Pattern.compile("[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]").matcher(word).find());
    }
}