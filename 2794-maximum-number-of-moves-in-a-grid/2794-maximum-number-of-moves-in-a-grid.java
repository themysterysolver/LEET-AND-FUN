class Solution {
    public int maxMoves(int[][] grid) {
        int row=grid.length;
        int col=grid[0].length;
        int[][] tabulation=new int[row][col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                tabulation[i][j]=-1;
            }
            tabulation[i][0]=0;
        }
        int[][] directions={{-1,-1},{0,-1},{1,-1}};
        for(int j=1;j<col;j++){
            for(int i=0;i<row;i++){
                for(int[] d:directions){
                    int nx=i+d[0];
                    int ny=j+d[1];
                    if(nx<0 || ny<0 || nx>=row || ny>=col )continue;
                    if(grid[nx][ny]<grid[i][j] && tabulation[nx][ny] != -1){
                        tabulation[i][j]=Math.max(tabulation[nx][ny]+1,tabulation[i][j]);
                    }
                }
            }
        }
        int maxi=0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                maxi = Math.max(tabulation[i][j], maxi);
            }
        }
        return maxi;
    }
}