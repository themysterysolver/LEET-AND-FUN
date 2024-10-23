/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private boolean BFS(TreeNode root,int x,int y){
        int l,i;
        Queue<Pair<TreeNode,TreeNode>> q=new LinkedList<>();
        q.add(new Pair<>(root,null));
        while(!q.isEmpty()){
            l=q.size();
            List<TreeNode> ans=new ArrayList<>();
            for(i=0;i<l;i++){
                Pair<TreeNode,TreeNode> current=q.poll();
                TreeNode r=current.getKey();
                TreeNode p=current.getValue();
                if(r.val==x||r.val==y){
                    if(p!=null){
                        ans.add(p);
                    }
                }
                if(r.left!=null){
                    q.add(new Pair<>(r.left,r));
                }
                if(r.right!=null){
                    q.add(new Pair<>(r.right,r));
                }
            }
            if(ans.size()==2 && ans.get(0)!=ans.get(1)){
                return true;
            }
        }
        return false;
    }
    public boolean isCousins(TreeNode root, int x, int y) {
        return BFS(root,x,y);
    }
}