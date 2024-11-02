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
    private List<List<Integer>> BFS(TreeNode root){
        List<List<Integer>> result=new ArrayList<>();
        if(root==null){
            return result;
        }
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        TreeNode r;
        int l,level=0,i;
        while(!q.isEmpty()){
            l=q.size();
            List<Integer> ans=new ArrayList<>();
            for(i=0;i<l;i++){
               r=q.poll();
               if(r.left!=null){
                    q.add(r.left);
               }
               if(r.right!=null){
                    q.add(r.right);
               }
                if(level%2==0){
                    ans.add(r.val);
                }
                else{
                    ans.add(0,r.val);
                }
            }
            result.add(ans);
            level++;
        }
        return result;
    }
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        return BFS(root);
    }
}