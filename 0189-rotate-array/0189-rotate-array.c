void display(int nums[],int numsSize){
    for(int i=0;i<numsSize;i++){
        printf("%d ",nums[i]);
    }
    printf("\n");
}
void reverse(int arr[],int start,int end){
    while(start<end){
        int temp=arr[end];
        arr[end]=arr[start];
        arr[start]=temp;
        start++;
        end--;
    }

}
void rotate(int* nums, int numsSize, int k) {
    k=k%numsSize;//efficent roation!!
    reverse(nums,0,numsSize-1);
    display(nums,numsSize);
    reverse(nums,0,k-1);
    display(nums,numsSize);
    reverse(nums,k,numsSize-1);
    display(nums,numsSize);
}