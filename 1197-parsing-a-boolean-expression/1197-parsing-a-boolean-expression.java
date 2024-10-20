class Solution {
    public boolean parseBoolExpr(String expression) {
        Stack<Character> stack=new Stack<>();
        Set<Character> bools=new HashSet<>();
        bools.add('t');bools.add('f');
        Set<Character> operators=new HashSet<>();
        operators.add('!');operators.add('|');operators.add('&');
        for(char s:expression.toCharArray()){
            if(operators.contains(s) || bools.contains(s)){
                stack.push(s);
            }
            else if(s==')'){
                Boolean containsTrue=false;
                Boolean containsFalse=false;
                while(!operators.contains(stack.peek())){
                    char top=stack.pop();
                    if(top=='t'){
                        containsTrue=true;
                    }
                    else if(top=='f'){
                        containsFalse=true;
                    }
                }
                char operatorForEvaluvation=stack.pop();
                if(operatorForEvaluvation=='!'){
                    stack.push(containsTrue ? 'f':'t');
                }
                else if(operatorForEvaluvation=='&'){
                    stack.push(containsFalse ? 'f':'t');
                }
                else{
                    stack.push(containsTrue ? 't':'f');
                }
            }
        }
        return stack.pop()=='t';
    }
}