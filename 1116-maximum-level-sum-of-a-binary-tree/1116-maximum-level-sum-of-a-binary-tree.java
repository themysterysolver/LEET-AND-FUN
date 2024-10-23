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
    private int BFS(TreeNode root){
        int i,l;
        Queue<TreeNode> q=new LinkedList<>();
        List<Integer> maximum=new ArrayList<>();
        maximum.add(root.val);
        q.add(root);
        while(!q.isEmpty()){
            l=q.size();
            int value=0;
            for(i=0;i<l;i++){
                TreeNode r=q.poll();
                if(r.left!=null){
                    value+=r.left.val;
                    q.add(r.left);
                }
                if(r.right!=null){
                    value+=r.right.val;
                    q.add(r.right);
                }
            }
            maximum.add(value);
        }
        maximum.remove(maximum.size()-1);
        int maxNum = Collections.max(maximum);
        return maximum.indexOf(maxNum) + 1;
    }
    public int maxLevelSum(TreeNode root) {
        if(root.left==null && root.right==null){
            return 1;
        }
        return BFS(root);
    }
}