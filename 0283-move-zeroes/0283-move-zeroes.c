void display(int nums[],int numsSize){
    for(int i=0;i<numsSize;i++){
        printf("%d ",nums[i]);
    }
    printf("\n");
}
void moveZeroes(int* nums, int numsSize) {
    int b[numsSize];
    int j=0;
    display(b,numsSize);
    for(int i=0;i<numsSize;i++){
       b[i]=0;
    }
    display(b,numsSize);
    for(int i=0;i<numsSize;i++){
       if(nums[i]!=0){
            b[j]=nums[i];
            j++;
       }
    }
    for(int i=0;i<numsSize;i++){
       nums[i]=b[i];
    }
    
}