class TrieNode{
    Map<Character,TrieNode> children;
    Boolean end;
    TrieNode(){
        children = new HashMap<>();
        end = false;
    }
}
class Trie{

    TrieNode root;
    Trie(){
        root = new TrieNode();
    }
    void insert(String s){
        TrieNode current = root;
        for(char c:s.toCharArray()){
            if (!current.children.containsKey(c)) {
                current.children.put(c, new TrieNode());
            }
            current = current.children.get(c);
        }
        current.end = true;
    }

    String LCP(){
        TrieNode curr = root;
        StringBuilder ans = new StringBuilder();
        while(true){
            if(curr.children.size()==1 && !curr.end){
                char key=curr.children.keySet().iterator().next();
                ans.append(key);
                curr = curr.children.get(key);
            }else{
                break;
            }
        }
        return ans.toString();
    }
    
}
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Trie t =new Trie();
        for(String s:strs){
            t.insert(s);
        }
        return t.LCP();
    }
}