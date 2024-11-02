import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Solution {
    public int myAtoi(String s) {
        Pattern pattern=Pattern.compile("^[\\ ]*([\\+\\-]?\\d+)");
        Matcher matcher=pattern.matcher(s);
        if(!matcher.find()){
            return 0;
        }
        String numStr=matcher.group(1);
        int i=0,sign=1;
        if(numStr.charAt(0)=='-'){
            sign=-1;
            i=1;
        }else if(numStr.charAt(0)=='+'){
            i=1;
        }
        long resNum=0;
        for(;i<numStr.length();i++){
            char ch=numStr.charAt(i);
            resNum=resNum*10+(ch-'0');
            if(resNum*sign>Integer.MAX_VALUE){
                return Integer.MAX_VALUE;
            }
            if (resNum*sign<Integer.MIN_VALUE){
                return Integer.MIN_VALUE;
            }
        }
        return (int)(resNum*sign);
    }
}