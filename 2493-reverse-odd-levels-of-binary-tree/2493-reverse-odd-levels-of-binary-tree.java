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
    private Queue<TreeNode> reverse(Queue<TreeNode> q){
        List<TreeNode> l= new ArrayList<>(q);
        int start=0,end=q.size()-1;
        while(start<end){
            int temp=l.get(start).val;
            l.get(start).val=l.get(end).val;
            l.get(end).val=temp;
            start++;
            end--;
        }
        Queue<TreeNode> newQ=new LinkedList<>(l);
        return newQ;
    }
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        q.offer(root);
        int lvl=0;
        while(!q.isEmpty()){
            int l=q.size();
            if(lvl%2==1){
                q=reverse(q);
            }
            for(int i=0;i<l;i++){
                TreeNode r=q.poll();
                if(r.left!=null){
                    q.offer(r.left);
                }
                if(r.right!=null){
                    q.offer(r.right);
                }
            }
            lvl++;
        }
        return root;
    }
}