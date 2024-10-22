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
    private long BFS(TreeNode root,int k){
        int l,i;
        PriorityQueue<Long> heap=new PriorityQueue<>();
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            l=q.size();
            long sum=0;
            for(i=0;i<l;i++){
                TreeNode r=q.poll();
                sum+=r.val;
                if(r.left!=null){q.add(r.left);}
                if(r.right!=null){q.add(r.right);}
            }
            heap.add(-sum);
        }
        for(i=0;i<k-1;i++){
            if(!heap.isEmpty()){
                heap.poll();
            }
        }
        if(!heap.isEmpty()){
            return -heap.poll();
        }
        else{
            return -1;
        }
    }
    public long kthLargestLevelSum(TreeNode root, int k) {
        return BFS(root,k);
    }
}