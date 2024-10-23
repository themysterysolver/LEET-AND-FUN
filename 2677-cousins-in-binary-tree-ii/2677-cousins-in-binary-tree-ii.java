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
    private List<Integer> BFS1(TreeNode root){
        int i,l,suml,levelsum;
        Queue<TreeNode> q=new LinkedList<>();
        List<Integer> levelSum=new ArrayList<>();
        q.add(root);
        while(!q.isEmpty()){
            l=q.size();
            suml=0;
            for(i=0;i<l;i++){
                TreeNode r=q.poll();
                suml+=r.val;
                if(r.left!=null){
                    q.add(r.left);
                }
                if(r.right!=null){
                    q.add(r.right);
                }
            }
            levelSum.add(suml);
        }
        return levelSum;
    }
    private TreeNode BFS2(TreeNode root,List<Integer> levelSum){
        int i,l,siblingSum,level=1;
        Queue<TreeNode> q=new LinkedList<>();
        root.val=0;
        q.add(root);
        while(!q.isEmpty()){
            l=q.size();
            for(i=0;i<l;i++){
                TreeNode r=q.poll();
                siblingSum=0;
                if(r.left!=null){
                    siblingSum+=r.left.val;
                }
                if(r.right!=null){
                    siblingSum+=r.right.val;
                }
                if(r.left!=null){
                    r.left.val=levelSum.get(level)-siblingSum;
                    q.add(r.left);
                }
                if(r.right!=null){
                    r.right.val=levelSum.get(level)-siblingSum;
                    q.add(r.right);
                }
            }
            level++;
        }
        return root;
    }
    public TreeNode replaceValueInTree(TreeNode root) {
        List<Integer> levelsum=BFS1(root);
        System.out.println(levelsum);
        return BFS2(root,levelsum);
    }
}