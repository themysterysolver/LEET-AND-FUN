class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        char[][] grid=new char[m][n];
        for(int i=0;i<m;i++){
            Arrays.fill(grid[i],' ');
        }
        for(int[] wall:walls){
            grid[wall[0]][wall[1]]='W';
        }
        for(int[] guard:guards){
            grid[guard[0]][guard[1]]='G';
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='G'){
                    //RIGHT
                    for(int k=j+1;k<n;k++){
                        if(grid[i][k]=='W' || grid[i][k]=='G')break;
                        grid[i][k]='B';
                    }// LEFT
                    for (int k=j-1;k>=0;k--) {
                        if(grid[i][k]=='W'||grid[i][k]=='G') break;
                        grid[i][k]='B';
                    }
                    // DOWN
                    for (int k=i+1;k<m;k++) {
                        if(grid[k][j]=='W' || grid[k][j]=='G') break;
                        grid[k][j] = 'B';
                    }
                    // UP
                    for (int k=i-1;k>=0;k--){
                        if(grid[k][j]=='W' || grid[k][j]=='G') break;
                        grid[k][j]='B';
                    }
                }
            }
        }
        int count=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++) {
                if(grid[i][j]==' ') {
                    count++;
                }
            }
        }
        return count;
    }
}