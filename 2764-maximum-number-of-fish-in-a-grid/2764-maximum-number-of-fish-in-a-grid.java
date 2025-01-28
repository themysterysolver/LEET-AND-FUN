class Solution {
    int row,col;
    boolean visited[][];
    int directions[][];
    int grid[][];
    private int BFS(int r,int c){
        visited[r][c]=true;
        int fish=0;
        Queue<int[]> q=new LinkedList<>();
        q.add(new int[]{r,c});
        while(!q.isEmpty()){
            int[] n=q.poll();
            int x=n[0];
            int y=n[1];
            fish+=grid[x][y];
            for(int pt=0;pt<directions.length;pt++){
                int nx=x+directions[pt][0];
                int ny=y+directions[pt][1];
                if(nx<0||ny<0||nx>=row||ny>=col||visited[nx][ny]){
                    continue;
                }
                else{
                    if(grid[nx][ny]>0){
                        visited[nx][ny]=true;
                        q.add(new int[]{nx,ny});
                    }
                }
            }
        }
        return fish;
    }
    public int findMaxFish(int[][] grid) {
        this.grid=grid;
        row=grid.length;
        col=grid[0].length;
        visited=new boolean[row][col];
        directions=new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
        int count=0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(grid[i][j]>0 && !visited[i][j]){
                    count=Math.max(count,BFS(i,j));
                }
            }
        }
        return count;
    }
}