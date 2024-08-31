char * mergeAlternately(char * word1, char * word2){
    int l1=strlen(word1);
    int l2=strlen(word2);
    printf("%d %d\n",l1,l2);
    for(int i=0;i<l1;i++){
        printf("%c ",word1[i]);
    }
    printf("\n");
    for(int i=0;i<l2;i++){
        printf("%c ",word2[i]);
    }
    printf("\n");
    int i=0,j=0;
    char* str=(char*)malloc(sizeof(char)*(l1+l2+1));
    int k=0;
    while(i<l1 && j<l2){
        str[k++]=word1[i++];
        str[k++]=word2[j++];
    }
    while(i<l1){
        str[k++]=word1[i++];
    }
    while(j<l2){
        str[k++]=word2[j++];
    }
    str[k]='\0';
    return str;
}