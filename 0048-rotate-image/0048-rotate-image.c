void display(int** matrix, int matrixSize, int* matrixColSize) {
    for(int i=0;i<matrixSize;i++){
        for(int j=0;j<*matrixColSize;j++){
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    display(matrix,matrixSize,matrixColSize);
    for(int i=0;i<matrixSize;i++){
        for(int j=i+1;j<*matrixColSize;j++){
            //printf("%d %d\n",i,j);
            int temp=matrix[i][j];
            matrix[i][j]=matrix[j][i];
            matrix[j][i]=temp;
        }
        //printf("\n");
    }
    //printf("\n");
    for(int i=0;i<matrixSize;i++){
        for(int j=0;j<*matrixColSize/2;j++){
            int temp=matrix[i][j];
            matrix[i][j]=matrix[i][*matrixColSize-1-j];
            matrix[i][*matrixColSize-1-j]=temp;
        }
    }
    display(matrix,matrixSize,matrixColSize);
    
}