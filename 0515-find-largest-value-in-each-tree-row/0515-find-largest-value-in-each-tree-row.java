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
    public int maxi(Queue<TreeNode> q){
        int maximum=Integer.MIN_VALUE;
        for(TreeNode a:q){
            maximum=Math.max(maximum,a.val);
        }
        return maximum;
    }
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> result=new ArrayList<>();
        if(root==null){
            return result;
        }
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            int l=q.size();
            result.add(maxi(q));
            for(int i=0;i<l;i++){
                TreeNode r=q.poll();
                if(r.left!=null){
                    q.add(r.left);
                }
                if(r.right!=null){
                    q.add(r.right);
                }
            }
        }
        return result;
    }
}