class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        double[] cost=new double[n];
        cost[start_node]=1;
        for(int i=0;i<n-1;i++){
            boolean changes=false;
            for(int j=0;j<edges.length;j++){
                int u=edges[j][0],v=edges[j][1];
                double edgeCost=succProb[j];
                if(edgeCost*cost[u]>cost[v]){
                    cost[v]=edgeCost*cost[u];
                    changes=true;
                }
                if(edgeCost*cost[v]>cost[u]){
                    cost[u]=edgeCost*cost[v];
                    changes=true;
                }
            }
            if(!changes){
                break;
            }
        }
        return cost[end_node];
    }
}
