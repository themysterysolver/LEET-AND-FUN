/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void push(int* stack,int i,int *top){
    (*top)++;
    stack[(*top)]=i;
}
void display(int *stack,int *top){
    for(int i=0;i<*top;i++){
        printf("%d ",stack[i]);
    }
}
int pop(int *stack,int *top){
    if(*top==-1)
        return -1;
    int temp=stack[(*top)];
    (*top)--;
    return temp;
}
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int *result;
    *returnSize=temperaturesSize;
    result=(int*)malloc(*returnSize*sizeof(int));
    int *stack=(int*)malloc(* returnSize*sizeof(int));
    for(int i=0;i<*returnSize;i++){
        result[i]=0;
        stack[i]=0;
    }
    int ltop=-1;
    for(int i=0;i<temperaturesSize;i++){
        printf("%d ",temperatures[i]);
    }
    printf("\n");
    for(int i=0;i<temperaturesSize;i++){
        while(ltop!=-1 && temperatures[i]>temperatures[stack[ltop]]){
            int index=pop(stack,&ltop);
            result[index]=i-index;
        }
        push(stack,i,&ltop);
    }
    display(stack,&ltop);
    printf("\n");
    for(int i=0;i<temperaturesSize;i++){
        printf("%d ",result[i]);
    }
    return result;
}