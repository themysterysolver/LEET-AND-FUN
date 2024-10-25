class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        System.out.println(folder);
        List<String> result=new ArrayList<>();
        for(String f:folder){
            boolean doesnotExist=true;
            for(String c:result){
                if(f.startsWith(c) && (f.length()==c.length() || f.charAt(c.length())=='/')){
                    doesnotExist=false;
                    break;
                }
            }
            if(doesnotExist){
                result.add(f);
            }
        }
        return result;
    }
}