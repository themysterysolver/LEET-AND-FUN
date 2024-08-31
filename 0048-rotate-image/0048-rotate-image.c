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
    //display(matrix,matrixSize,matrixColSize);
    int **d=(int**)malloc(matrixSize*sizeof(int*));
    for(int i=0;i<matrixSize;i++){
        d[i]=(int*)malloc(*matrixColSize*sizeof(int));
    }
    //new duplicated matrix!
    for(int i=0;i<matrixSize;i++){
        for(int j=0;j<*matrixColSize;j++){
            d[i][j]=matrix[i][j];
        }
    }
    //display(d,matrixSize,matrixColSize);
    for(int i=0;i<matrixSize;i++){
        for(int j=0;j<*matrixColSize;j++){
            d[j][*matrixColSize-1-i]=matrix[i][j];
        }
    }
    display(d,matrixSize,matrixColSize);
    for(int i=0;i<matrixSize;i++){
        for(int j=0;j<*matrixColSize;j++){
            matrix[i][j]=d[i][j];
        }
    }
    
}