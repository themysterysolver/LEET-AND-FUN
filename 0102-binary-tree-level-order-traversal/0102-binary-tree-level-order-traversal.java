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
        if(root==null){
            return new ArrayList<>();
        }
        int i,l;
        Queue<TreeNode> q=new LinkedList<>();
        List<List<Integer>> result=new ArrayList<>();
        q.add(root);
        while(!q.isEmpty()){
            List<Integer> levelList=new ArrayList<>();
            l=q.size();
            for(i=0;i<l;i++){
                TreeNode r=q.poll();
                levelList.add(r.val);
                if(r.left!=null){
                    q.add(r.left);
                }
                if(r.right!=null){
                    q.add(r.right);
                }
            }
            result.add(levelList);
        }
        return result;
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        return BFS(root);
    }
}